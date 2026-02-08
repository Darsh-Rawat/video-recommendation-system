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
          
def load_data_into_memory() : 
    dataset1_path = Path(__file__).resolve().parent.parent / "./data/dataset1.csv"
    dataset2_path = Path(__file__).resolve().parent.parent / "./data/dataset2.csv"
    
    data1 = pd.read_csv(f"{dataset1_path}")
    data2 = pd.read_csv(f"{dataset2_path}")
    
    data = pd.concat([data1, data2], ignore_index=True)
    data.drop(['Unnamed: 0', 'Unnamed: 7'], inplace=True, axis=1)
    
    return data
    


if __name__ == "__main__" :
    dataset1_path = Path(__file__).resolve().parent.parent / "./data/dataset1.csv"
    dataset2_path = Path(__file__).resolve().parent.parent / "./data/dataset2.csv"
    populate_collection(dataset1_path)
    populate_collection(dataset2_path)
