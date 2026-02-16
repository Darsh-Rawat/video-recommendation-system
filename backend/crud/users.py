from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import models.users as users_model
from core.security import get_password_hash, verify_password
from api.auth.schemas import LoginRequest, RegisterRequest

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

# def login_user(db: Session, loginRequest : LoginRequest) :
#     if loginRequest.email == None or loginRequest.password == None :
#         return 

#     if verify_password(loginRequest.password, )