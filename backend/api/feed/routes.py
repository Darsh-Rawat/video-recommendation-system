# FastAPI + SQLAlchemy Imports
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

# Dependencies import
from api.auth.dependencies import get_current_user
from db.session import get_db
from crud.feed import buildUserVector, searchVectorDB

# FastAPI Router
router = APIRouter(prefix="/feed")


# API Endpoint
@router.get("/search")
async def endpoint(db : Session = Depends(get_db), user : int = Depends(get_current_user)) : 
    user_embedding, excluded_ids = buildUserVector(user, db)
    return searchVectorDB(user_embedding, excluded_ids)