
from importlib.resources import path
from fastapi import APIRouter, Depends
import sqlalchemy
from database.database import get_db, engine
from database import to_db
from sqlalchemy.orm import Session
import csv


path=APIRouter()

@path.get("/export")
def export(db: Session = Depends(get_db)):
    metadata = sqlalchemy.MetaData()
    metadata.bind = engine
    mytable = sqlalchemy.Table('comments', metadata, autoload=True)
    db_connection = engine.connect()
    select = sqlalchemy.sql.select([mytable])
    result = db_connection.execute(select)
    fh = open('export/comment_export.csv', 'w')
    outcsv = csv.writer(fh)
    outcsv.writerow(result.keys())
    outcsv.writerows(result)
    fh.close
    return "export done"
    



    