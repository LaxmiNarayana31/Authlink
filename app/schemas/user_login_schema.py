from pydantic import BaseModel, EmailStr

class LoginSchema(BaseModel):
    email: str
    password: str

class LoginResponseSchema(BaseModel):
    name: str
    email: str
    access_token: str
    role: str