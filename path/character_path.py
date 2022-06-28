from fastapi import APIRouter
from models.characters_models import Character
from dal import characters_dal

path = APIRouter()

@path.get("/characters")
def get_characters()-> list[Character]:
    return characters_dal.get_characters()