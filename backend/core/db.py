import chromadb
import pandas as pd

# Initialize ChromaDB
client = chromadb.PersistentClient(path=r"D:\Code\video-recommendation-system\backend\data")

# Create or Get a collection
collection = client.get_or_create_collection(
    name="title_embeddings",
    metadata={"hnsw:space": "cosine"}
)

# Populate the collection if not populated
def populate_collection(dataset_path):
    if collection.count() == 0 : 
        data = pd.read_csv(f"{dataset_path}")

        titles = data["title"].tolist()
        ids = data["video_id"].tolist()
        
        collection.add(
            ids=ids,
            documents=titles,
        )
        print("Successfully Populated DB!")
    else : 
        print("DB Already Populated !")

if __name__ == "__main__" : 
    populate_collection(r"D:\Code\video-recommendation-system\backend\data\dataset1.csv")