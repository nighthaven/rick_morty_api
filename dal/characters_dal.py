from multiprocessing import connection
from models.characters_models import Character
from dal.connexion_helper import get_connection


def get_characters(in_progress:int, max_display:int)-> list[Character]:
    start = (in_progress * max_display) - max_display
    connection= get_connection()
    cursor = connection.cursor()
    query_characters = ("SELECT * FROM characters LIMIT %s OFFSET %s") % (max_display, start)
    cursor.execute(query_characters)
    data_characters = cursor.fetchall()
    return data_characters



