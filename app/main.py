from fastapi import Depends, FastAPI

from app.models.user import User, CreateUserRequest
from app.repository.users_repository import UsersRepository

app = FastAPI()

repo = UsersRepository()

def get_repository():
  yield repo

@app.post("/users/")
async def create_user(user: CreateUserRequest, repo: UsersRepository = Depends(get_repository)):
  created_user = User(repo.get_next_user_id(), user.name, user.birthday)
  repo.add_user(created_user)
  return created_user

@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int, repo: UsersRepository = Depends(get_repository)):
  user = repo.get_user_by_id(user_id)

  if user is not None:
    return user
  else:
    return {}

@app.put("/users/{user_id}")
async def update_user(user_id: int, repo: UsersRepository = Depends(get_repository)):
  return {}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, repo: UsersRepository = Depends(get_repository)):
  return {}

@app.get("/users/{user_id}/age")
async def get_age_of_user(user_id: int, repo: UsersRepository = Depends(get_repository)):
  return {}
