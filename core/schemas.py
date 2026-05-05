from pydantic import BaseModel,field_validator


class BaseModelPersonSchema(BaseModel):
    
    
    name:str
    @field_validator(name)
    def validation_name(cls,value):
        if len(value > 32):
            raise ValueError('name must not exceed 32 character')
        if value.isalpha():
            raise ValueError('name must only alphabeti character')
        return value
class PersonCreateSchema(BaseModelPersonSchema):
    
    age:int
    
    
    
class PresonResponseSchema(BaseModelPersonSchema):
    id:int
    
    
    
    
class PrsonUpdateSchema (BaseModelPersonSchema):
    pass