from pydantic import BaseModel

class UserData(BaseModel) : 
    video_id : str
    title : str