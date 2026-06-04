from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    house_id = Column(Integer, ForeignKey("houses.id", ondelete="CASCADE"), nullable=False)

    house = relationship("House", back_populates="rooms")
    #control_units = relationship("Control_unit", back_populates="room")
    #devices = relationship("Device", back_populates="room") начебто не потрібно томущо на кімнату має силатись дачик а не на впаки