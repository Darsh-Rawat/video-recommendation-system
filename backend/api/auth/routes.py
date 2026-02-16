# /login route
# /login register
# /login route
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.users import find_user_from_email, register_user_to_db
from api.auth.schemas import LoginRequest, RegisterRequest
from db.session import get_db

router = APIRouter(prefix="/auth")

@router.post("/register")
async def endpoint(registerRequest : RegisterRequest, db: Session = Depends(get_db)) : 
    if find_user_from_email(db, registerRequest.email) : 
        return {"message" : "User already exists"}
    return register_user_to_db(db, registerRequest)

@router.post("/login")
async def endpoint(loginRequest : LoginRequest, db: Session = Depends(get_db)) : 
    ...
