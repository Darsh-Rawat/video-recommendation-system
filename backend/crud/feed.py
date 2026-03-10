# FastAPI + SQLAlchemy Imports
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# Numpy
import numpy as np
from datetime import datetime

# Vector DB imports
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
from core.db import collection
from chromadb import Embeddings

# Model imports
import models.users as users_model

# Embedding function setup 
ef = DefaultEmbeddingFunction()

# Setup
half_life = 1 # In days, after how much days the value falls to half
lam = np.log(2) / half_life

# Functions

def calculate_weights(time : list) -> list : 
    now = datetime.now()
    weights = []
    
    for t in time : 
        age_days = ((now - t) / (24 * 3600)).days
        age_days = max(0, age_days)
        w = np.exp(-lam * age_days)
        weights.append(w)
    return weights

def buildUserVector(userId : int, db : Session) -> Embeddings: 
    last_5_videos = db.query(users_model.UserInteractionData.video_id, users_model.UserInteractionData.watched_at).filter(users_model.UserInteractionData.user_id == userId).order_by(users_model.UserInteractionData.watched_at.desc()).limit(15).all()
    # last_5_id = [id for (id,time) in last_5_videos]
    # recency = [time for (id,time) in last_5_videos]
    last_5_id = []
    recency = []
    for id, time in last_5_videos :
        if id not in last_5_id : 
            last_5_id.append(id)
            recency.append(time)
    
    # Fetch embeddings for last 5 videos
    item_embeddings = collection.get(ids=last_5_id, include=["embeddings"])
    
    # Weights are the recency for each video
    weights = calculate_weights(recency)
    
    # Matrix multiply weights with item embeddings and divide it by sum of weights
    user_vector = np.average(item_embeddings["embeddings"], weights=weights, axis=0)
    
    return user_vector, last_5_id

def searchVectorDB(user_embedding : Embeddings, excluded_ids : list) -> list: 
    relevant_videos = collection.query(query_embeddings=[user_embedding], where={"ids": {"$nin": excluded_ids}}, n_results=50)
    feed_videos = []
    for i in range(len(relevant_videos['ids'][0])) :
        video = {}
        if relevant_videos['ids'][0][i] not in excluded_ids : 
            video['video_id'] = relevant_videos['ids'][0][i]
            video['title'] = relevant_videos['documents'][0][i]
            feed_videos.append(video)
    return feed_videos