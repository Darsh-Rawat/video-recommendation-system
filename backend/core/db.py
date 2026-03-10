import chromadb
import pandas as pd
from pathlib import Path
import json

# Video_IDs
FILE_PATH = Path("data/video_ids.json")

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
    data1['published_at'] = pd.to_datetime(data1['published_at'])

    data2 = pd.read_csv(f"{dataset2_path}")
    data2['published_at'] = data2['published_at'].astype(str) + "T00:00:00Z"
    data2['published_at'] = pd.to_datetime(data2['published_at'])

    
    data = pd.concat([data1, data2], ignore_index=True)
    data.drop(['Unnamed: 0', 'Unnamed: 7'], inplace=True, axis=1)
    
    if FILE_PATH.exists():
        print("video_ids.json already exists. Skipping creation.")
    else:
        VIDEO_IDS = list(set(data["video_id"]))  # remove duplicates if any

        with open(FILE_PATH, "w") as f:
            json.dump(VIDEO_IDS, f, indent=4)


    print("video_ids.json created successfully.")
    

    data['published_at'] = pd.to_datetime(data['published_at'])
    data['views'] = data['views'].astype(int)
    data = data[['video_id', 'title', 'channel_name', 'views', 'likes', 'comments', 'keyword', 'published_at']]
    print(data['video_id'].duplicated().sum())
    data.drop_duplicates(subset=['video_id'], inplace=True)
    print(data['video_id'].duplicated().sum())
    data.to_csv("data/dataset.csv", index=False)
    
    return data
    
    

if __name__ == "__main__" :
    dataset1_path = Path(__file__).resolve().parent.parent / "./data/dataset1.csv"
    dataset2_path = Path(__file__).resolve().parent.parent / "./data/dataset2.csv"
    populate_collection(dataset1_path)
    populate_collection(dataset2_path)
