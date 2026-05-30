from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    house_id = Column(Integer, ForeignKey("houses.id"))
    name = Column(String, nullable=False)

    house = relationship("House", back_populates="rooms")
    control_units = relationship("Control_unit", back_populates="room")
    divaces = relationship("Divace", back_populates="room")