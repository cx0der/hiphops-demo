from app.models.user import User

class UsersRepository():
  users: list[User]

  def __init__(self):
    self.users = list[User]()

  def add_user(self, user: User) -> int:
    self.users.append(user)
    return user.id

  def get_user_by_id(self, id: int) -> User | None:
    for u in self.users:
      if u.id == id:
        return u
    return None

  def get_next_user_id(self) -> int:
    return len(self.users) + 1
