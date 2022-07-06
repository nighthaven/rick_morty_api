from pydantic import BaseModel

class Episode(BaseModel):
    episode_id:int
    ep_name:str
    air_date:str
    episode_num:str
    characters:str