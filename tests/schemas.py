from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

class UserListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[User]

class UserResponse(BaseModel):
    data: User

class CreateUserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str

class UpdateUserResponse(BaseModel):
    name: str
    job: str
    updatedAt: str

class RegisterResponse(BaseModel):
    id: int
    token: str

class ErrorResponse(BaseModel):
    error: str