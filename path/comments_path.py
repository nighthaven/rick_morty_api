from fastapi import APIRouter,status, Query
from dal import comments_dal
from fastapi.params import Depends
from database.database import get_db
from sqlalchemy.orm import Session
from models import comments_models
from security.security import get_current_user
from models.users_models import User



path=APIRouter()

@path.post("/comments", status_code=status.HTTP_201_CREATED)
def add_comment(request:comments_models.Comment , db: Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return comments_dal.add_comment(request,db)

@path.put("/comments/{id}")
def update_comment(id:int, request:comments_models.Comment, db: Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    comment.user_id = current_user.user_id
    return comments_dal.update_comment(id, request,db)

@path.delete("/comments/{id}")
def delete_comment(id:int, db: Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    comment.user_id = current_user.user_id
    return comments_dal.delete_comment(id,db)

@path.get("/comments")
def get_comments(start:int = Query(1), max_display:int=Query(5), db: Session = Depends(get_db)):
    return comments_dal.get_comments(start, max_display, db)

@path.get("/comments/character={id}")
def get_comments_by_character(id, db: Session = Depends(get_db)):
    return comments_dal.get_comments_by_character(id,db)


@path.get("/comments/episode={episode_id}")
def get_comments_by_episode(episode_id:int, db: Session = Depends(get_db)):
    return comments_dal.get_comments_by_episode(episode_id,db)

@path.get("/comments/character={id}/by")
def get_comments_by_character_in_episode(id:int,episode:int, db: Session = Depends(get_db)):
    return comments_dal.get_comments_by_character_in_episode(id,episode,db)

@path.get("/comments/filter={message}")
def get_comments_by_filter(message:str, db: Session = Depends(get_db)):
    return comments_dal.get_comments_by_filter(message,db)

