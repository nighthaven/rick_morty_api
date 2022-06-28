from models.characters_models import Character
from dal.connexion_helper import get_connexion


def get_characters()-> list[Character]:
    cursor=get_connexion().cursor()
    cursor.execute("SELECT * FROM characters")
    query_characters=cursor.fetchall()
    return query_characters

