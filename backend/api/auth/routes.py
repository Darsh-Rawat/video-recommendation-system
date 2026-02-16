# /login route
# /login register
# /login route
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from crud.users import find_user_from_email, register_user_to_db, login_user
from api.auth.dependencies import get_current_user
from core.security import create_token, ACCESS_TOKEN_EXPIRE_MINUTES
from api.auth.schemas import LoginRequest, RegisterRequest
from db.session import get_db

router = APIRouter(prefix="/auth")

@router.post("/register")
async def endpoint(registerRequest : RegisterRequest, db: Session = Depends(get_db)) : 
    if find_user_from_email(db, registerRequest.email) : 
        return {"message" : "User already exists"}
    return register_user_to_db(db, registerRequest)

@router.post("/login")
async def endpoint(loginRequest : LoginRequest, response:Response, db: Session = Depends(get_db)) : 
    user = login_user(db, loginRequest)
    if user is None : 
        raise HTTPException(status_code=401, detail="Invalid Credentials")
   
    token = create_token(
        data={'sub':str(user.user_id)}
    )
    response.set_cookie( key="access_token", 
                        value=token, 
                        httponly=True, 
                        secure=False, 
                        samesite="lax", 
                        max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60)
