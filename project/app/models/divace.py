from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False, unique=True)
    value_device = Column(String(20), nullable=False) # Виправили divace -> device
    
    kind_id = Column(Integer, ForeignKey("device_kinds.id"), nullable=False)
    
    # Зв'язок назад з кімнатою. back_populates має вказувати на "devices" (в множині)
    room = relationship("Room", back_populates="devices")
    
    # ТИМЧАСОВО КОМЕНТУЄМО (поки не створимо ці моделі):
    device_kind = relationship("Device_kind", back_populates="devices")
    telemetrys = relationship("Telemetry", back_populates="device")