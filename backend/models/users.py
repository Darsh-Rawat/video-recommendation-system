from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from db.session import Base

# ============== SQL Models ==============
class Users(Base) : 
    __tablename__ = "user_data"
    
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

class UserInteractionData(Base) : 
    __tablename__ = "user_interaction_data"
    
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    video_id = Column(String, primary_key=True, index=True)
    video_title = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())