from pydantic import BaseModel

class InteractionData(BaseModel) : 
    user_id : int
    username : str
    video_id : str
    video_title : str 
    
class VideoDetails(BaseModel) : 
    video_id : str
    video_title : str