from core.db import collection

# Get Videos ID based on query
def get_videos(query:str) -> list :
    result = collection.query(
        query_texts=[f"{query}"],
        n_results=5
    )    
    return result['documents'][0]



     
