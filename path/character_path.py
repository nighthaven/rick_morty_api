from fastapi import APIRouter, Query
from models.characters_models import Character
from dal import characters_dal

path = APIRouter()

@path.get("/characters")
def get_characters(in_progress:int=Query(1),max_display:int=Query(10))-> list[Character]:
    return characters_dal.get_characters(in_progress, max_display)