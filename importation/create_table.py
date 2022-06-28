import sqlite3
mydb = sqlite3.connect('rickmorty.db')

cursor = mydb.cursor()

cursor.execute("DROP TABLE IF EXISTS comments")
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("DROP TABLE IF EXISTS characters")
cursor.execute("DROP TABLE IF EXISTS episodes")


cursor.execute("CREATE TABLE characters(\
    character_id INTEGER PRIMARY KEY NOT NULL,\
    charac_name VARCHAR(50) NOT NULL,\
    status VARCHAR(7) NOT NULL,\
    species VARCHAR(50) NOT NULL,\
    charac_type VARCHAR(50),\
    gender VARCHAR(10) NOT NULL,\
    charac_ep VARCHAR(255) NOT NULL\
    )")

cursor.execute("CREATE TABLE episodes(\
    episode_id INTEGER PRIMARY KEY NOT NULL,\
    ep_name VARCHAR(100) NOT NULL,\
    air_date VARCHAR(50) NOT NULL,\
    episode_num VARCHAR(6) NOT NULL,\
    charaters TEXT NOT NULL\
    )")

cursor.execute("CREATE TABLE users(\
    user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
    user_name VARCHAR(100) NOT NULL)")

cursor.execute("CREATE TABLE comments(\
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
    user_id INTEGER NOT NULL,\
    character_id INTEGER,\
    episode_id INTEGER,\
    message TEXT NOT NULL,\
    FOREIGN KEY (user_id) REFERENCES users(user_id))")

cursor.execute("CREATE INDEX index_character ON comments (character_id);")
cursor.execute("CREATE INDEX index_episode ON comments (episode_id);")



print("TABLE CREATED")

mydb.commit()
