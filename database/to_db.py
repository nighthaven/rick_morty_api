from sqlalchemy import Column, Integer, String, ForeignKey
from database.database import Base
from sqlalchemy.orm import relationship

class Characters(Base):
    __tablename__ = "characters"
    character_id = Column(Integer, primary_key=True, index=True)
    charac_name = Column(String)
    status = Column(String)
    species = Column(String)
    charac_type = Column(String)
    gender = Column(String)
    charac_ep = Column(String)

class Episodes(Base):
    __tablename__ = "episodes"
    episode_id	= Column(Integer, primary_key=True, index=True)
    ep_name = Column(String)
    air_date = Column(String)
    episode_num = Column(String)
    charaters = Column(String)

class Comments(Base):
    __tablename__ = "comments"
    comment_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    character_id = Column(Integer)
    episode_id = Column(Integer)
    message = Column(String)

class Users(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    user_type = Column(String)
    password = Column(String)