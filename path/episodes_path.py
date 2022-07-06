from fastapi import APIRouter
from dal import episodes_dal
from fastapi.params import Depends
from database.database import get_db
from sqlalchemy.orm import Session

path = APIRouter()

@path.get("/episodes")
def get_episodes(db: Session = Depends(get_db)):
    return episodes_dal.get_episodes(db)