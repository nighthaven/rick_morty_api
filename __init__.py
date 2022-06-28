from fastapi import FastAPI
from path.character_path import path as path_characters
from path.episodes_path import path as path_episodes

app=FastAPI()
app.include_router(path_characters)
app.include_router(path_episodes)

@app.get("/")
def root():
    return "Merci a Rick, à Morty, à Savannah et a Sebastien pour me permettre de faire ce test.\
    mais surtout a Brice Andreota qui m'a rendu suffisemment autonome pour en arriver la\
    en esperant bien sur que je puisse devenir developer back end. Merci à Jellysmack\
    plus generalement."