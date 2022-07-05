from fastapi import FastAPI
from path.character_path import path as path_characters
from path.episodes_path import path as path_episodes
from path.comments_path import path as path_comments
from path.users_path import path as path_user
from path.login_path import path as path_login

app = FastAPI()
app.include_router(path_characters)
app.include_router(path_episodes)
app.include_router(path_comments)
app.include_router(path_user)
app.include_router(path_login)

@app.get("/")
def root():
    return "Merci a Rick, à Morty, à Savannah et a Sebastien pour me permettre de faire ce test.\
    mais surtout a Brice Andreota qui m'a rendu suffisamment autonome pour en arriver la\
    en esperant bien sur que je puisse devenir developer back end un jour. Merci à Jellysmack\
    plus generalement."