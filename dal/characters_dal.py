from fastapi.params import Depends
from database.database import get_db
from sqlalchemy.orm import Session
from database import to_db

def get_characters(db: Session = Depends(get_db)):
    characters = db.query(to_db.Characters).all()
    return characters
