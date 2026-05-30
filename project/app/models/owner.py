from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Owner(Base):
    __tablename__ = "owners"  # Так таблиця буде називатися в базі даних

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    person_nomber = Column(Integer, unique=True, nullable=False)

    # Вказуємо SQLAlchemy, що цей користувач пов'язаний із завданнями.
    # back_populates="owner" означає, що в класі Task буде змінна owner,
    # яка вказує назад на цього користувача.
    houses = relationship("House", back_populates="owner")