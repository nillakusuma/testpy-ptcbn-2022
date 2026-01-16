from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MasterBase(BaseModel):
    name: str
    description: Optional[str] = None

class MasterCreate(MasterBase):
    pass

class MasterResponse(MasterBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True