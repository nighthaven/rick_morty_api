import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="jellysmack_exam",
    auth_plugin="mysql_native_password"
)
cursor=mydb.cursor()

cursor.execute("DROP TABLE IF EXISTS characters")
cursor.execute("DROP TABLE IF EXISTS episodes")

cursor.execute("CREATE TABLE characters(\
    character_id INT PRIMARY KEY NOT NULL,\
    charac_name VARCHAR(50) NOT NULL,\
    status VARCHAR(7) NOT NULL,\
    species VARCHAR(50) NOT NULL,\
    type VARCHAR(50),\
    gender VARCHAR(10) NOT NULL,\
    charac_ep VARCHAR(255) NOT NULL\
    )")

cursor.execute("CREATE TABLE episodes(\
    episode_id INT PRIMARY KEY NOT NULL,\
    ep_name VARCHAR(100) NOT NULL,\
    air_date VARCHAR(50) NOT NULL,\
    episode VARCHAR(6) NOT NULL,\
    charaters TEXT NOT NULL\
    )")

mydb.commit()

print("TABLE CREATED")