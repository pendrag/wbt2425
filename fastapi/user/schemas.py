from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    role: int = 0

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True