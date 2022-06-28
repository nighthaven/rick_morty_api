import sqlite3


def get_connexion():
    return sqlite3.connect('rickmorty.db', check_same_thread=False)