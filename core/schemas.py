from pydantic import BaseModel,field_validator,Field,field_serializer


class BaseModelPersonSchema(BaseModel):
    
    firstname:str = Field(...,description='enter Persons name')
    lastname : str = Field(...,description='enter Persons name')
    
    @field_validator('firstname')
    def validation_name(cls,value):
        if len(value) > 32:
            raise ValueError('name must not exceed 32 character')
        if not value.isalpha():
            raise ValueError('name must only alphabeti character')
        return value
    
    
    @field_serializer('firstname')
    def serialize_name(cls,value):
        return value.title()
    
class PersonCreateSchema(BaseModelPersonSchema):
    age:int =  Field(...,description='Id of Person')
    
    
    
class PresonResponseSchema(BaseModelPersonSchema):
    id:int = Field(...,description='Id of Person')
    
    
    
    
    
class PrsonUpdateSchema (BaseModelPersonSchema):
    pass