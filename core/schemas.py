from pydantic import BaseModel, field_validator, Field, field_serializer

class BasePersonSchema(BaseModel):
    name: str = Field(..., description="Enter the name of the person")

    @field_validator("name")
    def validate_name(cls, value):
        if len(value) > 32:
            raise ValueError("The name must not exceed 32 chars")
        if not value.isalpha():
            raise ValueError("The name must only contain alphabetic chars")
        return value 
    
    @field_serializer("name")
    def serialize_name(self, value):
        return value.title()
            
    
    
class PersonCreateSchema(BasePersonSchema):
    pass
    
class PersonResponseSchema(BasePersonSchema):
    id: int


class PersonUpdateSchema(BasePersonSchema):
    name: str
    