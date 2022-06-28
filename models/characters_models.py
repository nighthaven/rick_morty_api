from pydantic import BaseModel,Field

class Character(BaseModel):
    character_id:int=Field(...)
    charac_name:str=Field(...)
    status:str=Field(...)
    species:str=Field(...)
    charac_type:str=Field(...)
    gender:str=Field(...)
    charac_ep:str=Field(...)

