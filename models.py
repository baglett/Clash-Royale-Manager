from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ClanMember(BaseModel):
    tag: str = Field(..., max_length=20)
    name: str = Field(..., max_length=100)
    role: str = Field(..., max_length=50)
    trophies: int
    donations: int
    last_seen: datetime
    join_date: datetime
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None