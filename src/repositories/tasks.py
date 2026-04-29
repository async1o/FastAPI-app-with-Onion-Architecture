from utils.repositories import SQLAlchemyRepositories
from models.tasks import TasksModel


class TasksRepositories(SQLAlchemyRepositories):
    model = TasksModel
