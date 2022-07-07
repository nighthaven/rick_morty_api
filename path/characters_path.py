from fastapi import APIRouter, Query
from dal import characters_dal
from fastapi.params import Depends
from database.database import get_db
from sqlalchemy.orm import Session

path = APIRouter()

@path.get('/characters')
def get_characters(start:int = Query(1), max_display:int=Query(5), db: Session = Depends(get_db)):
    return characters_dal.get_characters(start, max_display, db)