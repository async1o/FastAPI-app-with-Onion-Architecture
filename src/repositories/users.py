from src.utils.repositories import SQLAlchemyRepositories
from src.models.users import UsersModel

class UserRepositories(SQLAlchemyRepositories):
    model = UsersModel