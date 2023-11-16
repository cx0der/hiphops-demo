from pydantic import BaseModel
from uuid import uuid4 as uuid

class CreateUserRequest(BaseModel):
  name: str
  birthday: str

class User:

  def __init__(self, id: int, name: str, birthday: str):
    self.id = id
    self.name = name
    self.birthday = birthday
    self.is_active = True
