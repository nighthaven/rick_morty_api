from fastapi.params import Depends
from database.database import get_db
from sqlalchemy.orm import Session
from database import to_db

def get_characters(start:int, max_display:int, db: Session = Depends(get_db)):
    return db.query(to_db.Characters)\
        .limit(max_display)\
        .offset((start*max_display)-max_display)\
        .all()