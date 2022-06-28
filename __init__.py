from fastapi import FastAPI
from path.character_path import path as path_characters

app=FastAPI()
app.include_router(path_characters)

@app.get("/")
def root():
    return "Merci a Rick, à Morty, mais surtout a Brice Andreota qui m'a rendu suffisemment autonome pour en arriver la\
    en esperant bien sur que je puisse devenir developer back end. Merci à Jellysmack\
    pour me permettre de faire ce test."