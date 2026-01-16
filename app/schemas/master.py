from pydantic import BaseModel
from datetime import datetime

# Schema untuk input create
class MasterCreate(BaseModel):
    name: str
    description: str

# Schema untuk update
class MasterUpdate(BaseModel):
    name: str | None = None
    description: str | None = None

# Schema untuk output / response
class MasterOut(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime

    class Config:
        from_attributes = True   # di Pydantic v2, ganti orm_mode
