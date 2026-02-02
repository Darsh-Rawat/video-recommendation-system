from core.db import collection

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




     
