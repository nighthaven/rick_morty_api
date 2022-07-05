from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    user_id:Optional[int] = Field()
    user_name:str = Field(...)
    user_type:str = Field(...)
    user_password:str = Field(...)

class DisplayUser(BaseModel):
    user_name:str
    user_type:str
    class Config:
        orm_mode=True
