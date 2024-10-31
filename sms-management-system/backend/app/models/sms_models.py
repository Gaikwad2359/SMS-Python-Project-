from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from datetime import datetime

# Helper class for MongoDB ObjectId fields
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

# Data model for SMS Configuration (stored in MongoDB)
class CountryOperatorConfig(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    country: str
    operator: str
    high_priority: bool = False
    active: bool = True
    success_rate: Optional[float] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "country": "India",
                "operator": "Airtel",
                "high_priority": True,
                "active": True,
                "success_rate": 95.5,
            }
        }

# Data model for SMS Metrics (stored in MySQL)
class SMSMetrics(BaseModel):
    id: Optional[int]
    country_operator_id: int
    timestamp: datetime
    sent: int = 0
    successful: int = 0
    failed: int = 0
    success_rate: Optional[float] = None

    class Config:
        schema_extra = {
            "example": {
                "country_operator_id": 1,
                "timestamp": "2024-10-31T10:00:00",
                "sent": 100,
                "successful": 95,
                "failed": 5,
                "success_rate": 95.0,
            }
        }
