from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class User(Base):
    __tablename__ = "users"  # Так таблиця буде називатися в базі даних

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Вказуємо SQLAlchemy, що цей користувач пов'язаний із завданнями.
    # back_populates="owner" означає, що в класі Task буде змінна owner,
    # яка вказує назад на цього користувача.
    tasks = relationship("Task", back_populates="owner")