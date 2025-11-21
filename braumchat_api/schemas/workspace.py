from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WorkspaceCreate(BaseModel):
    name: str
    slug: Optional[str] = None

class WorkspaceRead(BaseModel):
    id: int
    name: str
    slug: str
    owner_id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
