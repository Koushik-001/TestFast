from pydantic import BaseModel

class UserSchema(BaseModel):
    email:str
    name:str
    mobile:str

class UpdateUserSchema(BaseModel):
    email:str = None
    name:str = None
    mobile:str = None