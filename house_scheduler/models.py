from datetime import datetime

from pydantic import BaseModel


class Task(BaseModel):
    id: int
    name: str
    description: str = ""
    start: datetime
    end: datetime | None = None
    repeat: str = ""
    all_day: bool = False
