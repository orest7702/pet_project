from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Control_unit(Base):
    __tablename__ = "control_units"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))
    name = Column(String, nullable=False)

    room = relationship("Room", back_populates="control_units")