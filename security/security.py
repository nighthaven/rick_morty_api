from fastapi import APIRouter, Depends, status, HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database.database import get_db
from database import to_db
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from models.token_models import TokenData


SECRET_KEY = "9ae820b69efb998332d7766567e1239578cf4405d4979de57e4bae7750312909"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1200

router=APIRouter()

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def generate_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt =jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(to_db.Users).filter(to_db.Users.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Username not found / invalid user")
    if not pwd_context.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid password")
    access_token = generate_token(
        data={"sub":user.username}
    )
    return {"access_token":access_token,"token_type":"bearer"}

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
    detail="invalid credential",
    headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        username:str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    #recup utilisateur dans base de données 
    user=db.query(to_db.Users).filter(to_db.Users.username == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user


