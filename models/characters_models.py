from pydantic import BaseModel

class character(BaseModel):
    character_id:int
    charac_name:str
    status:str
    species:str
    charac_type:str
    gender:str
    charac_ep:str
