from datetime import datetime

from croniter import croniter
from pydantic import BaseModel, validator


class Task(BaseModel):
    id: int
    name: str
    description: str = ""
    start: datetime
    end: datetime | None = None
    repeat: str = ""
    all_day: bool = False

    @validator("repeat")
    def validate_repeat(cls, v):
        if v == "" or croniter.is_valid(v):
            return v
        else:
            return ValueError("crontab is invalid")
