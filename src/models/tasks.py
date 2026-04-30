from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from db.db import Base
from schemas.tasks import TasksSchema


class TasksModel(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    performer: Mapped["UsersModel"] = relationship(  # noqa
        back_populates="tasks", lazy="selectin"
    )

    def to_read_model(self) -> TasksSchema:
        return TasksSchema(task_id=self.id, text=self.text, owner_id=self.owner_id)
