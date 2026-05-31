from pydantic import BaseModel, Field
from typing import Optional

class OwnerBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    first_name: Optional[str] = Field(None, max_length=50)
    person_nomber: int = Field(...)

class OwnerCreate(OwnerBase):
    pass

class OwnerUpdate(OwnerBase):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    first_name: Optional[str] = Field(None, max_length=50)
    person_nomber: int = Field(None)

class OwnerResponse(OwnerBase):
    id: int

    class Config:
        from_attributes = True