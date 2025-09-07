from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class SeverityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class StatusEnum(str, Enum):
    pending = "pending"
    verified = "verified"
    resolved = "resolved"

class HazardReportCreate(BaseModel):
    latitude: float
    longitude: float
    type: str
    severity: SeverityEnum
    description: Optional[str] = None

class HazardReportResponse(BaseModel):
    id: str
    latitude: float
    longitude: float
    type: str
    severity: str
    status: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    timestamp: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class StatusUpdate(BaseModel):
    status: StatusEnum