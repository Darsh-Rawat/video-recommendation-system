from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import models.users as users_model
from core.security import get_password_hash, verify_password, create_token
from api.auth.schemas import LoginRequest, RegisterRequest
from schemas.users_interaction import VideoDetails

def register_user_to_db(db: Session, registerRequest : RegisterRequest) : 
    hashed_pwd = get_password_hash(registerRequest.password)
    user_info = users_model.Users(
        username = registerRequest.username,
        email = registerRequest.email,
        password = hashed_pwd
    )
    try : 
        db.add(user_info)
        db.commit()
        db.refresh(user_info)
        return user_info
    except SQLAlchemyError as e : 
        db.rollback()
        print(e)

def find_user_from_email(db: Session, email) :
    return db.query(users_model.Users).filter(users_model.Users.email == email).first()

def login_user(db: Session, loginRequest : LoginRequest) :
    user = find_user_from_email(db, loginRequest.email)
    if not user:
        return None
    if not verify_password(loginRequest.password, user.password):
        return None
    return user

def store_user_interaction(db: Session, videoDetails : VideoDetails, user_id) :
    if not db : 
        return False
    username = db.query(users_model.Users).filter(users_model.Users.user_id == user_id).first().username

    interaction_data = users_model.UserInteractionData(
        user_id = user_id,
        username = username,
        video_id = videoDetails.video_id,
        video_title = videoDetails.video_title
    )
    try : 
        db.add(interaction_data)
        db.commit()
        db.refresh(interaction_data)
        return interaction_data
    except SQLAlchemyError as e : 
        db.rollback()
        print(e)
    