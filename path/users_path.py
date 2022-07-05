from fastapi import APIRouter, status
from models.users_models import User, DisplayUser
from dal import users_dal

path=APIRouter()

@path.post("/users",response_model=DisplayUser,status_code = status.HTTP_201_CREATED)
def create_comment(user:User) -> None:
    users_dal.create_user(user)