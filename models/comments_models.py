from  pydantic import BaseModel, Field, validator, ValidationError
from typing import Optional

class Comment(BaseModel):
    comment_id:Optional[int] = Field()
    user_id:Optional[int] = Field()
    character_id:Optional[int] = Field()
    episode_id:Optional[int] = Field()
    message:str = Field(...)

    @validator("message")
    def mandatory_information(cls,v, values, **kwargs):
        if not values["character_id"] and not values["episode_id"]:
            raise ValueError('comment must be linked to at list one character or episode')
        return v