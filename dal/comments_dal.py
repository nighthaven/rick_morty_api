from fastapi import HTTPException, status
from fastapi.params import Depends
from database.database import get_db
from sqlalchemy.orm import Session
from models import comments_models
from database import to_db
from security.security import get_current_user
from models.users_models import User


def add_comment(request:comments_models.Comment , db: Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    new_comment = to_db.Comments(
        comment_id=request.comment_id, 
        user_id=current_user.user_id,
        character_id=request.character_id,
        episode_id=request.episode_id,
        message=request.message
        )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return request

def update_comment(id:int, request:comments_models.Comment, db: Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    request.comment_id = id
    comment = db.query(to_db.Comments).filter(to_db.Comments.comment_id == id)
    if not comment:
        pass
    comment.update(request.dict())
    db.commit()
    return "comment successfully updated"

def delete_comment(id:int, db: Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    db.query(to_db.Comments).filter(to_db.Comments.comment_id == id).delete(synchronize_session=False)
    db.commit()
    return "comment deleted"

def get_comments(start:int, max_display:int, db: Session = Depends(get_db)):
    return db.query(to_db.Comments)\
    .limit(max_display)\
    .offset((start*max_display)-max_display)\
    .all()

def get_comments_by_character(id, db: Session = Depends(get_db)):
    comments = db.query(to_db.Comments).filter(to_db.Comments.character_id == id).all()
    if not comments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="comment(s) not found")
    return comments

def get_comments_by_episode(episode_id:int, db: Session = Depends(get_db)):
    comments = db.query(to_db.Comments).filter(to_db.Comments.episode_id == episode_id).all()
    if not comments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="comment(s) not found")
    return comments

def get_comments_by_character_in_episode(id:int,episode:int, db: Session = Depends(get_db)):
    comments = db.query(to_db.Comments).filter(to_db.Comments.character_id == id).filter(to_db.Comments.episode_id == episode).all()
    if not comments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="comment(s) not found")
    return comments

def get_comments_by_filter(message:str, db: Session = Depends(get_db)):
    comments = db.query(to_db.Comments).filter(to_db.Comments.message.like("%"+message+"%")).all()
    if not comments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="comment(s) not found")
    return comments