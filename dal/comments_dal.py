from dal.connexion_helper import get_connection
from models.comment_models import Comment

def create_comment(comment:Comment) -> None:
    connection = get_connection()
    cursor = connection.cursor()
    creation_comment = "INSERT INTO comments(user_id, character_id, episode_id, message)\
    VALUES (%s,%s,%s,'%s');" % (comment.user_id,comment.character_id or "Null",comment.episode_id or "Null",comment.message)
    cursor.execute(creation_comment)
    connection.commit()

