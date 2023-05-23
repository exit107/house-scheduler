from datetime import datetime

from pydantic import ValidationError

from models import Task

task_data = {
    "id": 1,
    "name": "clean office",
    "description": "clean the office",
    "start": datetime.now(),
    "end": datetime.now(),
    "repeat": "",
    "all_day": False,
}

try:
    task = Task(**task_data)
    print(task)
except ValidationError as e:
    print(e)

task_data_with_crontab = {
    "id": 2,
    "name": "clean kitchen",
    "description": "clean the kitchen",
    "start": datetime.now(),
    "end": datetime.now(),
    "repeat": "@weekly",
    "all_day": False,
}

try:
    task2 = Task(**task_data_with_crontab)
    print(task2)
except ValidationError as e:
    print(e)