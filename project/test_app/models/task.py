from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)  # nullable=True означає, що може бути порожнім
    is_completed = Column(Boolean, default=False)

    # Зовнішній ключ: зберігає id користувача з таблиці users
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Зв'язок для Python: дозволяє отримати об'єкт User через task.owner
    owner = relationship("User", back_populates="tasks")