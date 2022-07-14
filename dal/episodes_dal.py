from fastapi.params import Depends
from database.database import get_db
from sqlalchemy.orm import Session
from database import to_db

def get_episodes(db: Session = Depends(get_db)):
    episodes = db.query(to_db.Episodes).all()
    return episodes

    