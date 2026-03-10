from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, TIMESTAMP, func, ForeignKey, BigInteger
from db.session import Base

class Videos(Base):
    __tablename__ = "videos"
    video_id = Column(String, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    channel_name = Column(String, nullable=False)
    views = Column(BigInteger, nullable=False)
    likes = Column(BigInteger, nullable=False)
    comments = Column(BigInteger, nullable=False)  
    keyword = Column(String, nullable=False)
    published_at = Column(TIMESTAMP)
    
    interactions = relationship("UserInteractionData", back_populates="video")