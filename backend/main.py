from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from core.helper_funcs import get_videos, store_user_data, retrieve_candidates, search_video
from core.db import load_data_into_memory
from core.models import UserData


@asynccontextmanager
async def lifespan(app : FastAPI) : 
    data = load_data_into_memory()
    app.state.data = data
    print("INFO : Dataset Loaded into memory...")
    
    yield
    
    del app.state.data
    print("INFO : Dataset Unloaded into memory...")

origins = [
    "http://localhost:5173",
]

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/search/{query}")
# async def endpoint(query:str) : 
#     return get_videos(query)

@app.get("/search/")
async def endpoint(query:str) : 
    return search_video(query, app.state.data)
    return get_videos(query)

@app.post("/watch")
async def endpoint(userData: UserData) : 
    # print(type(userData.video_id))
    # print(type(userData.title))
    store_user_data(userData.video_id, userData.title)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",reload=True)