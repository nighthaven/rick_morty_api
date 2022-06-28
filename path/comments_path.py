from fastapi import APIRouter, status
from models.comment_models import Comment
from dal import comments_dal

path = APIRouter()

@path.post("/comments",status_code = status.HTTP_201_CREATED)
def create_comment(comment:Comment) -> None:
    comments_dal.create_comment(comment)