from pydantic import BaseModel,field_validator,Field,field_serializer


class BaseModelPersonSchema(BaseModel):
    
    name:str = Field(...,description='enter Persons name')
    
    @field_validator(name)
    def validation_name(cls,value):
        if len(value > 32):
            raise ValueError('name must not exceed 32 character')
        if value.isalpha():
            raise ValueError('name must only alphabeti character')
        return value
    
    
    @field_serializer('name')
    def serialize_name(value):
        return value.title()
    
class PersonCreateSchema(BaseModelPersonSchema):
    age:int =  Field(...,description='Id of Person')
    
    
    
class PresonResponseSchema(BaseModelPersonSchema):
    id:int = Field(...,description='Id of Person')
    
    
    
    
    
class PrsonUpdateSchema (BaseModelPersonSchema):
    pass