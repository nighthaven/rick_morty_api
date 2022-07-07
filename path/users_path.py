from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from database import to_db
from passlib.context import CryptContext
from dal import users_dal
from models import users_models

path=APIRouter()

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated="auto")

@path.post("/users")
def create_user(request:users_models.User, db: Session = Depends(get_db)):
    return users_dal.create_user(request, db)


