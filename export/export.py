from importlib.resources import path
from fastapi import APIRouter, Depends
from database.database import get_db
from database import to_db
from sqlalchemy.orm import Session
import pandas


path=APIRouter()

@path.get("/export")
def export_comment(db: Session = Depends(get_db)):
    query_comments=db.query(to_db.Comments).all()
    return query_comments

"""    comment_id = [data[0] for data in data_comments]
    user_id = [data[1] for data in data_comments]
    character_id = [data[2] for data in data_comments]
    episode_id = [data[3] for data in data_comments]
    message = [data[4] for data in data_comments]
    data_to_transform = {"comment_id": comment_id, "user_id": user_id, "character_id": character_id, "episode_id": episode_id, "message": message}
    data_to_pandas = pandas.DataFrame(data_to_transform)
    return data_to_pandas.to_csv("export/comment.csv")"""

    
    



    