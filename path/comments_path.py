from fastapi import APIRouter, Depends, Query, status, HTTPException
from models.comment_models import Comment
from models import users_models
from dal import comments_dal
from path.login_path import get_current_user

path = APIRouter()

@path.post("/comments",status_code = status.HTTP_201_CREATED)
def create_comment(comment:Comment, current_user:users_models.User = Depends(get_current_user)) -> None:
    comment.user_id = current_user.user_id
    comments_dal.create_comment(comment)

@path.put("/comments/{comment_id}")
def edit_comment(comment_id:int,comment:Comment, current_user:users_models.User = Depends(get_current_user))-> None:
    comments_dal.edit_comment(comment_id,comment)

@path.delete("/comments/{comment_id}")
def delete_comment(comment_id:int, current_user:users_models.User = Depends(get_current_user))-> None:
    comments_dal.delete_comment(comment_id)

@path.get("/comments")
def get_comments(in_progress:int=Query(1), max_display:int=Query(5))->list[Comment]:
    return comments_dal.get_comments(in_progress, max_display)

@path.get("/comments/ep={episode_id}")
def get_comments_by_episode(episode_id:int)-> list[Comment]:
    if not episode_id :
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="id must not be blank")
    return comments_dal.get_comments_by_episode(episode_id)

@path.get("/comments/ch={character_id}")
def get_comments_by_character(character_id:int)-> list[Comment]:
    if not character_id :
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="id must not be blank")
    return comments_dal.get_comments_by_character(character_id)

@path.get("/comments/ch={character_id}")
def get_comments_by_character_in_episode(character_id:int,episode_id:int)-> list[Comment]:
    if not character_id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="id must not be blank")
    return comments_dal.get_comments_by_character_in_episode(character_id,episode_id)

@path.get("/comments/filter={message}")
def get_comments_by_filter_message(message:str)-> list[Comment]:
    if not message:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Filter can't be empty")
    return comments_dal.get_comments_by_filter_message(message)


