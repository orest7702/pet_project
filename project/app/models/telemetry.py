from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from app.models.base import Base

class Telemetry(Base):
    __tablename__ = "telemetrys"

    id = Column(Integer, primary_key=True, index=True)
    divace_id = Column(Integer, ForeignKey("divaces.id"), nullable=False)
    fire = Column(Boolean, nullable=True)
    pressure = Column(Integer, nullable=True)
    temperature = Column(Float, nullable=True) # Змінив на Float для градусів
    humidity = Column(Integer, nullable=True)
    
    divaces = relationship("Divace", back_populates="telemetrys")