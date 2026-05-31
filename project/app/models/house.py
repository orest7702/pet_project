from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class House(Base):
    __tablename__ = "houses"
    
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("owners.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, unique=True, nullable=False)
    
    owner = relationship("Owner", back_populates="houses")
    rooms = relationship("Room", back_populates="house")