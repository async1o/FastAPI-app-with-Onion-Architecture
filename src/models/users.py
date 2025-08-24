from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship


from src.db.db import Base
from src.schemas.users import UserSchema
from src.models.tasks import TasksModel

class UsersModel(Base):
    __tablename__ = 'users'

    id : Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    tasks: Mapped[List['TasksModel']] = relationship(back_populates='performer',lazy='selectin')

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            user_id=self.id,
            username=self.username,
            email=self.email,
            password=self.password,
            tasks=[model.to_read_model() for model in self.tasks]
        )