import socket

from core.db import collection
from core.postgre import get_connection, release_connection

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
        




     
