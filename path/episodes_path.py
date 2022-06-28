from fastapi import APIRouter
from models.episodes_models import Episode
from dal import episodes_dal

path=APIRouter()

@path.get("/episodes")
def get_episodes() -> list[Episode]:
    return episodes_dal.get_episodes()