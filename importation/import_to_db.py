import sqlite3
import json
mydb = sqlite3.connect('rickmorty.db')

cursor = mydb.cursor()


file_characters = open("importation/rick_morty_characters_v1.json")
data_characters = json.load(file_characters)

file_episodes = open("importation/rick_morty_episodes_v1.json")
data_episodes = json.load(file_episodes)

cursor.execute("DELETE FROM characters")
cursor.execute("DELETE FROM episodes")

sql_base_characters = "INSERT INTO characters VALUES"

sql_values_characters = ["(%s,'%s','%s','%s','%s','%s','%s')" % (
    dictionary.get("id"),
    dictionary.get("name").replace("'","''"),
    dictionary.get("status"),
    dictionary.get("species"),
    dictionary.get("type").replace("'","''"),
    dictionary.get("gender"),
    dictionary.get("episode")
) for dictionary in data_characters]

sql_result_characters = f"{sql_base_characters} {', '.join(sql_values_characters)};"

sql_base_episodes = "INSERT INTO episodes VALUES"

sql_values_episodes = ["(%s,'%s','%s','%s','%s')" % (
    dictionary.get("id"),
    dictionary.get("name").replace("'","''"),
    dictionary.get("air_date"),
    dictionary.get("episode"),
    dictionary.get("characters")
) for dictionary in data_episodes]


sql_result_episodes = f"{sql_base_episodes} {', '.join(sql_values_episodes)};"

cursor.execute(sql_result_characters)
cursor.execute(sql_result_episodes)

print(cursor.rowcount, "database imported")

mydb.commit()

#TODO "DATE_FORMAT(" + dictionary.get("air_date")+", %machin)",
