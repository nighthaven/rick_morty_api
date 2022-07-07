from fastapi import Depends
from database.database import get_db
from database import to_db
from sqlalchemy.orm import Session
from models import users_models
from passlib.context import CryptContext

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated="auto")

def create_user(request:users_models.User, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    new_user = to_db.Users(
        user_id=request.user_id, 
        username=request.username, 
        user_type=request.user_type,
        password=hashed_password,
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request

