from fastapi import APIRouter
from dal import characters_dal
from fastapi.params import Depends
from database.database import get_db
from sqlalchemy.orm import Session

path = APIRouter()

@path.get('/characters')
def get_characters(db: Session = Depends(get_db)):
    return characters_dal.get_characters(db)