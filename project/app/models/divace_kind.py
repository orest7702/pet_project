from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Divace_kind(Base):
    __tablename__ = "divace_kinds"  

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)
    unit = Column(String(20), nullable=False)
    marking = Column(String)
    
    divaces = relationship("Divace", back_populates="divace_kind")