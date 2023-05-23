from datetime import datetime

from models import Task

task_data = {
    "id": 1,
    "name": "clean office",
    "description": "clean the office",
    "start": datetime.now(),
    "end": datetime.now(),
    "repeat": "",
    "all_day": False
}

task = Task(**task_data)
print(task)
