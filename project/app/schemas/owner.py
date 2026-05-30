from pydantic import BaseModel, Field
from typing import Optional

class OwnerBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    first_name: Optional[str] = Field(..., max_length=50)
    person_nomber: Optional[str] = Field(..., max_length=20)
    
class OwnerCreate(OwnerBase):
    pass

class OwnerUpdate(OwnerBase):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    first_name: Optional[str] = Field(None, max_length=50)
    person_nomber: Optional[str] = Field(None, pattern=r"^\d{12}$")

class OwnerResponse(OwnerBase):
    id: int

    class Config:
        from_attributes = True