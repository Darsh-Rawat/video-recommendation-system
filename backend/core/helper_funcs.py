import math
import socket
import pandas as pd
from datetime import date, datetime
from dateutil import parser

from sqlalchemy import func

from core.db import collection
from db.session import fetch_db_session
from models.videos import Videos

def retrieve_candidates(query: str) -> dict:
    result = collection.query(
    query_texts=[f"{query}"],
    n_results=20
    )
    
    return result

# def rank_candidates(candidates: dict, max_views, similarity: dict, video_stats: list[Videos]) -> list:
#     # final_score = {}
#     ranking = {}
    
#     for video in video_stats:
#         # Similarity Score
#         similarity_score = similarity[video.video_id]
        
#         # Popularity Score
#         pop_score = 0
#         views_score = math.log10(video.views + 1) / math.log10(max_views + 1)

#         like_ratio = video.likes / (video.views + 1)
#         likes_score = min(like_ratio / 0.1, 1.0) 

#         pop_score = (0.7 * views_score) + (0.3 * likes_score)
        
#         # Recency Score
#         # ! Need to fix parser parsing already converted datatime
#         recency_score = 0
#         # start_date = parser.parse(video['published_at']).date()
#         start_date = (video.published_at).date()
#         recency_score = 1/((date.today() - start_date).days + 1)
        
#         # Final Score
#         final_score = 0
#         final_score = ((similarity_score * 0.7) + (pop_score * 0.2) + (recency_score * 0.1))
        
        
#         video['ranking_score'] = final_score
        
    
#     video_stats.sort(key=lambda x: x['ranking_score'], reverse=True)

#     return video_stats

def rank_candidates(candidates: dict, max_views, similarity: dict, video_stats):

    def score(video):
        # Similarity
        similarity_score = similarity.get(video.video_id, 0)

        # Popularity
        views_score = math.log10(video.views + 1) / math.log10(max_views + 1)

        like_ratio = video.likes / (video.views + 1)
        likes_score = min(like_ratio / 0.1, 1.0)

        pop_score = (0.7 * views_score) + (0.3 * likes_score)

        # Recency
        start_date = video.published_at.date()
        recency_score = 1 / ((date.today() - start_date).days + 1)

        # Final score
        final_score = (
            (similarity_score * 0.7) +
            (pop_score * 0.2) +
            (recency_score * 0.1)
        )

        return final_score

    ranked_videos = sorted(video_stats, key=score, reverse=True)

    return ranked_videos
        

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
        similarity[ids[i]] = 1 - semantic_relevance[i]
   
    with fetch_db_session() as db : 
        video_stats = db.query(Videos).filter(Videos.video_id.in_(ids)).all()
        max_views = db.query(func.max(Videos.views)).scalar()
                
    return rank_candidates(candidates, max_views, similarity, video_stats)
    

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


