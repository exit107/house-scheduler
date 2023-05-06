from datetime import datetime

from pprint import pprint
from schemas import TaskSchema
from models import Task

task = Task('clean office', 'clean the office', datetime.now(), datetime.now())
pprint(task)