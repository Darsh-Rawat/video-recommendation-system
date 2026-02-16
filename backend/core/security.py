# Password hashing and JWT Token Logic here
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 100

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def create_token(data:dict) : 
    to_encode = data.copy()
    expire = datetime.now(ZoneInfo('Asia/Kolkata')) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token) : 
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) 
        return payload["sub"] 
    except JWTError: 
        return None