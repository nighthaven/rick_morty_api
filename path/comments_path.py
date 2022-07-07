from fastapi import APIRouter,status
from dal import comments_dal
from fastapi.params import Depends
from database.database import get_db
from sqlalchemy.orm import Session
from models import comments_models



path=APIRouter()

@path.post("/comments", status_code=status.HTTP_201_CREATED)
def add_comment(request:comments_models.Comment , db: Session = Depends(get_db)):
    return comments_dal.add_comment(request,db)

@path.put("/comments/{id}")
def update_comment(id:int, request:comments_models.Comment, db: Session = Depends(get_db)):
    return comments_dal.update_comment(id, request,db)

@path.delete("/comments/{id}")
def delete_comment(id:int, db: Session = Depends(get_db)):
    return comments_dal.delete_comment(id,db)

@path.get("/comments")
def get_comments(db: Session = Depends(get_db)):
    return comments_dal.get_comments(db)

@path.get("/comments/character={id}")
def get_comments_by_character(id, db: Session = Depends(get_db)):
    return comments_dal.get_comments_by_character(id,db)


@path.get("/comments/episode={episode_id}")
def get_comments_by_episode(episode_id:int, db: Session = Depends(get_db)):
    return comments_dal.get_comments_by_episode(episode_id,db)

@path.get("/comments/character={id}/by")
def get_comments_by_character_in_episode(id:int,episode:int, db: Session = Depends(get_db)):
    return comments_dal.get_comments_by_character_in_episode(id,episode,db)

