from pydantic import BaseModel,Field


class BaseModelPersonSchema(BaseModel):
    name:str
class PersonCreateSchema(BaseModelPersonSchema):
    
    age:int
    
    
    
class PresonResponseSchema(BaseModelPersonSchema):
    id:int
    
    
    
    
class PrsonUpdateSchema (BaseModelPersonSchema):
    pass