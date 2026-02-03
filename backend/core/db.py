import chromadb
import pandas as pd
from pathlib import Path

# Initialize ChromaDB
db_path = Path(__file__).resolve().parent.parent / "./data/chromadb"
client = chromadb.PersistentClient(path=db_path)

# Create or Get a collection
collection = client.get_or_create_collection(
    name="title_embeddings",
    metadata={"hnsw:space": "cosine"}
)

# Populate the collection if not populated
def populate_collection(dataset_path):

    data = pd.read_csv(f"{dataset_path}")

    titles = data["title"].tolist()
    ids = data["video_id"].tolist()
    
    collection.add(
        ids=ids,
        documents=titles,
    )
    print("Successfully Populated DB!")


if __name__ == "__main__" :
    dataset1_path = Path(__file__).resolve().parent.parent / "./data/dataset1.csv"
    dataset2_path = Path(__file__).resolve().parent.parent / "./data/dataset2.csv"
    populate_collection(dataset1_path)
    populate_collection(dataset2_path)
