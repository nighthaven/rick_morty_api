from fastapi import FastAPI
from path.characters_path import path as path_character
from path.episodes_path import path as path_episode
from database import to_db
from database.database import engine

app=FastAPI()
app.include_router(path_character)
app.include_router(path_episode)

to_db.Base.metadata.create_all(engine)

app.get("/")
def root():
    return "Merci a Rick, à Morty, à Savannah et a Sebastien pour me permettre de faire ce test.\
    mais surtout a Brice Andreota qui m'a rendu suffisamment autonome pour en arriver là\
    en esperant bien sur que je puisse devenir developer back end un jour. Merci à Jellysmack\
    plus generalement."

