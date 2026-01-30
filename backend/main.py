from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.helper_funcs import get_videos

origins = [
    "http://localhost:5173",
]

app = FastAPI()

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
    return get_videos(query)
    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",reload=True)