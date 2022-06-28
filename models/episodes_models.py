from pydantic import BaseModel, Field

class Episode(BaseModel):
    episode_id:int=Field(...)
    ep_name:str=Field(...)
    air_date:str=Field(...)
    epidose_num:str=Field(...)
    characters:str=Field(...)
