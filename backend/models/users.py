from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, TIMESTAMP, func, ForeignKey
from db.session import Base

# ============== SQL Models ==============
class Users(Base) : 
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    
    interactions = relationship("UserInteractionData", back_populates="user")
    
class UserInteractionData(Base) : 
    __tablename__ = "user_interaction_data"
    
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True, index=True)
    video_id = Column(String, ForeignKey("videos.video_id"), primary_key=True, nullable=False)
    watched_at = Column(TIMESTAMP, server_default=func.now())
    
    user = relationship("Users", back_populates="interactions")
    video = relationship("Videos", back_populates="interactions")

# class SyntheticData(Base) : 
#     __tablename__ = "synthetic_interaction_data"
    
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer)
#     username = Column(String(50), nullable=False)
#     video_id = Column(String, nullable=False)
#     created_at = Column(TIMESTAMP)