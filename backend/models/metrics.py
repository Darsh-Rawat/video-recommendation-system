from sqlalchemy import Column, Integer, String, TIMESTAMP, func, Boolean
from db.session import Base

# ============== SQL Models ==============
class Impressions(Base) : 
    __tablename__ = "impressions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    user_query = Column(String, nullable=False)
    video_id = Column(String, nullable=False)
    video_title = Column(String, nullable=False)
    rank = Column(Integer, nullable=False)
    is_watched = Column(Boolean, default=False, nullable=False)