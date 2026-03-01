from fastapi import Request
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import models.metrics as metrics_model
from db.session import get_db
from api.auth.dependencies import get_current_user

def store_metrics(search_results : list, user_query : str, user_id : int) : 
    objects = []
        
    db = next(get_db())
    if not db : 
        raise SQLAlchemyError("Database connection not found")
    
    for rank,video in enumerate(search_results) : 
        data = metrics_model.Impressions(
            user_id = user_id,
            user_query = user_query,
            video_id = video["video_id"],
            video_title = video["title"],
            rank = rank
        )
        objects.append(data)
        db.add(data)
    try : 
        db.commit()
        for obj in objects:
            db.refresh(obj)
    except SQLAlchemyError as e : 
        db.rollback()
        print(e)

def update_stored_metrics(db : Session, videoDetails, user : int) : 
    if not db :
        raise SQLAlchemyError("Database connection not found")

    db.query(metrics_model.Impressions).filter(metrics_model.Impressions.user_id == user).filter(metrics_model.Impressions.video_id == videoDetails.video_id).update({"is_watched" : True})
    try : 
        db.commit()
    except SQLAlchemyError as e : 
        db.rollback()
        print(e)