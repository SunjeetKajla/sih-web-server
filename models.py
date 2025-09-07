from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class HazardReport(BaseModel):
    id: Optional[str] = None
    latitude: float
    longitude: float
    type: str
    severity: str
    status: str = "pending"
    description: Optional[str] = None
    image_url: Optional[str] = None
    timestamp: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True