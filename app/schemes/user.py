from typing import Literal
import re

from pydantic import BaseModel, field_validator, EmailStr


class UserInput(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Literal['user', 'admin']

    @field_validator('password')
    def password_validate(cls, value : str) -> str:
        pattern = '^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$'

        if re.match(pattern=pattern, string=value) or len(value) >= 100:
            raise ValueError('Username or password does not match')
        
        return value
    
    @field_validator('username')
    def username_validate(cls, value : str) -> str:
        if len(value) < 5 or len(value) >= 50:
            raise ValueError('Username validation error')
        
class UserOutput(BaseModel):
    id: int
    username: str
    email: EmailStr