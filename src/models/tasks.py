from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.db.db import Base
from src.schemas.tasks import TasksSchema

class TasksModel(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]   
    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    performer: Mapped["UsersModel"] = relationship(back_populates='tasks', lazy='selectin') #type: ignore

    def to_read_model(self) -> TasksSchema:
        return TasksSchema(
            user_id=self.id,
            text=self.text,
            owner_id=self.owner_id
        )