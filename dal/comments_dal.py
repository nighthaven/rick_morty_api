from dal.connexion_helper import get_connection
from models.comment_models import Comment

def create_comment(comment:Comment) -> None:
    connection = get_connection()
    cursor = connection.cursor()
    creation_comment = "INSERT INTO comments(user_id, character_id, episode_id, message) VALUES (%s,%s,%s,'%s');" \
    % (comment.user_id,comment.character_id or "Null",comment.episode_id or "Null",comment.message)
    cursor.execute(creation_comment)
    connection.commit()

def edit_comment(comment_id:int,comment:Comment)-> None:
    connection = get_connection()
    cursor = connection.cursor()
    edit_comment = "UPDATE comments SET user_id=%s, character_id=%s, episode_id=%s, message='%s' WHERE comment_id=%s;" \
    % (comment.user_id or "1", 
    comment.character_id or "Null",
    comment.episode_id or "Null",
    comment.message or "inserez votre message",
    comment_id)
    cursor.execute(edit_comment)
    connection.commit()

def delete_comment(comment_id:int)-> None:
    connection = get_connection()
    cursor = connection.cursor()
    delete_comment = "DELETE FROM comments WHERE comment_id=%s;" % (comment_id)
    cursor.execute(delete_comment)
    connection.commit()

def get_comments(in_progress:int, max_display:int) -> list[Comment]:
    start = (in_progress * max_display) - max_display
    connection = get_connection()
    cursor = connection.cursor()
    query_comments=("SELECT * FROM comments LIMIT %s OFFSET %s") % (max_display, start)
    cursor.execute(query_comments)
    data_comments = cursor.fetchall()
    return data_comments    


def get_comments_by_episode(episode_id:int)-> list[Comment]:
    connection = get_connection()
    cursor = connection.cursor()
    query_comments_by_episode=("SELECT * FROM comments WHERE episode_id=%s;" % (episode_id))
    cursor.execute(query_comments_by_episode)
    query_comments = cursor.fetchall()
    return query_comments

def get_comments_by_character(character_id:int)-> list[Comment]:
    connection = get_connection()
    cursor = connection.cursor()
    query_comments_by_character=("SELECT * FROM comments WHERE character_id=%s;" % (character_id))
    cursor.execute(query_comments_by_character)
    query_comments = cursor.fetchall()
    return query_comments

def get_comments_by_character_in_episode(character_id:int,episode_id:int)-> list[Comment]:
    connection = get_connection()
    cursor = connection.cursor()
    query_comments_by_character_in_episode=("SELECT * FROM comments WHERE (character_id=%s AND episode_id=%s);"
    % (character_id,episode_id))
    cursor.execute(query_comments_by_character_in_episode)
    query_comments = cursor.fetchall()
    return query_comments

def get_comments_by_filter_message(message:str)-> list[Comment]:
    connection = get_connection()
    cursor = connection.cursor()
    query_comments_by_filter_message="SELECT * FROM comments WHERE message LIKE '%s'" % ("%"+message+"%")
    cursor.execute(query_comments_by_filter_message)
    query_comments = cursor.fetchall()
    return query_comments