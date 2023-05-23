from datetime import datetime


class Task:
    def __init__(
        self,
        name,
        description: str,
        start,
        end: datetime,
        repeat: str = "",
        all_day: bool = False,
    ) -> None:
        self.name = name
        self.description = description
        self.start = start
        self.end = end
        self.repeat = repeat
        self.all_day = all_day

    def __repr__(self) -> str:
        return f"<Task({self.name})>"
