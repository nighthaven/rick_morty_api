from importlib.resources import path
from fastapi import APIRouter
from dal.connexion_helper import get_connection
import pandas


path=APIRouter()

@path.get("/export")
def export_comment():
    connection = get_connection()
    cursor = connection.cursor()
    query_comments=("SELECT * FROM comments")
    cursor.execute(query_comments)
    data_comments = cursor.fetchall()
    comment_id = [data[0] for data in data_comments]
    user_id = [data[1] for data in data_comments]
    character_id = [data[2] for data in data_comments]
    episode_id = [data[3] for data in data_comments]
    message = [data[4] for data in data_comments]
    data_to_transform = {"comment_id": comment_id, "user_id": user_id, "character_id": character_id, "episode_id": episode_id, "message": message}
    data_to_pandas = pandas.DataFrame(data_to_transform)
    return data_to_pandas.to_csv("export/comment.csv")

    
    



    