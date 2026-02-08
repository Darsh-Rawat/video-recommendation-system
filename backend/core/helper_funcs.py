import math
import socket
import pandas as pd
from datetime import date, datetime
from dateutil import parser

from core.db import collection
from core.postgre import get_connection, release_connection

def retrieve_candidates(query: str) -> dict:
    result = collection.query(
    query_texts=[f"{query}"],
    n_results=10
    )
    
    return result

def rank_candidates(candidates: dict, similarity: dict, video_stats: list[dict]) -> list:
    # final_score = {}
    
    for video in video_stats:
        # Similarity Score
        similarity_score = similarity[video["video_id"]]
        
        # Popularity Score
        pop_score = 0
        pop = (math.log10(video["views"] + 1)/7) * (1+(video["likes"]/(video["views"] + 100)))
        pop_score = min(pop, 1)
        
        # Recency Score
        recency_score = 0
        start_date = parser.parse(video['published_at']).date()
        recency_score = 1/((date.today() - start_date).days + 1)
        
        # Final Score
        final_score = 0
        final_score = ((similarity_score * 0.6) + (pop_score * 0.2) + (recency_score * 0.1))
        
        video['ranking_score'] = final_score
        
    
    
    video_stats.sort(key=lambda x: x['ranking_score'], reverse=True)
    
    return video_stats
        

# ================ TEMP FUNCTIONS ================
def search_video(query: str, data) -> list:
    """
    This a temporary function which will replace the get_videos function
    """
    
    candidates = retrieve_candidates(query)
    
    ids = candidates["ids"][0]
    semantic_relevance = candidates["distances"][0]
    similarity = {}
    
    for i in range(len(ids)) : 
        similarity[ids[i]] = semantic_relevance[i]
    
    video_stats = data.loc[data['video_id'].isin(ids)].to_dict(orient='records')
    
    return rank_candidates(candidates, similarity, video_stats)
    

# Get Videos ID based on query
def get_videos(query:str) -> list :
    result = collection.query(
        query_texts=[f"{query}"],
        n_results=10
    )   
    ids = result["ids"][0]
    titles = result["documents"][0]
        
    videos = []

    for i in range(len(ids)):
        videos.append({
            "id": ids[i],
            "title": titles[i],
        })
        
    return videos

# Store the user data for the Phase-2
def store_user_data(video_id:str, title:str) -> None : 
    conn = get_connection()
    username = str(socket.gethostname())
    try:
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO user_data (username, video_id, title)
            VALUES (%s, %s, %s)
            """,
            (username, video_id, title)
        )
        conn.commit()
    finally:
        release_connection(conn)
        




     
