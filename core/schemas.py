from pydantic import BaseModel, field_validator

class BasePersonSchema(BaseModel):
    name: str

    @field_validator("name")
    def validtae_name(cls, value):
        if len(value) > 32:
            raise ValueError("The name must not exceed 32 chars")
        if not value.isalpha():
            raise ValueError("The name must only contain alphabetic chars")
        return value 
    
class PersonCreateSchema(BasePersonSchema):
    pass
    
class PersonResponseSchema(BasePersonSchema):
    id: int


class PersonUpdateSchema(BasePersonSchema):
    name: str
    