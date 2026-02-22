from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from slowapi import Limiter
from slowapi.util import get_remote_address
from sqlalchemy.orm import Session

from core.helper_funcs import get_videos, store_user_data, retrieve_candidates, search_video
from core.db import load_data_into_memory
from api.auth.dependencies import get_current_user
from db.session import Base, engine
from db.session import get_db

from api.auth.routes import router as auth_router
from schemas.users_interaction import VideoDetails
from crud.users import store_user_interaction

Base.metadata.create_all(bind=engine)
@asynccontextmanager
async def lifespan(app : FastAPI) : 
    data = load_data_into_memory()
    app.state.data = data
    print("INFO : Dataset Loaded into memory...")
    
    yield
    
    del app.state.data
    print("INFO : Dataset Unloaded into memory...")

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173"
]

app = FastAPI(lifespan=lifespan)
app.include_router(auth_router)
limiter = Limiter(key_func=get_remote_address)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search/")
@limiter.limit("10/minute")
async def endpoint(query:str, request : Request) : 
    return search_video(query, app.state.data)

@app.post("/watch")
async def endpoint(videoDetails: VideoDetails, user : dict = Depends(get_current_user), db : Session = Depends(get_db)) : 
    store_user_interaction(db, videoDetails, user)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0", port=8000, reload=True)