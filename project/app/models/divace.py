from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Divace(Base):
    __tablename__ = "divaces"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    kind_id = Column(Integer, ForeignKey("divace_kinds.id"), nullable=False)
    name = Column(String, nullable=False, unique=True)
    value_divace = Column(String(20), nullable=False)
    
    room = relationship("Room", back_populates="divaces")
    divace_kind = relationship("Divace_kind", back_populates="divaces")
    telemetrys = relationship("Telemetry", back_populates="divaces")