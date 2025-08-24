from src.utils.repositories import SQLAlchemyRepositories
from src.models.tasks import TasksModel


class TasksRepositories(SQLAlchemyRepositories):
    model = TasksModel