from models.episodes_models import Episode
from dal.connexion_helper import get_connection


def get_episodes() -> list[Episode]:
    cursor = get_connection().cursor()
    cursor.execute("SELECT * FROM episodes")
    query_episodes = cursor.fetchall()
    return query_episodes