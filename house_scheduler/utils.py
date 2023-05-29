"""
Utilities for managing tasks
"""

from pathlib import Path
from typing import List, TextIO

from pydantic import ValidationError
import yaml

from models import Task


class TaskFile(object):
    def __init__(self, filename: str) -> None:
        self.tasks: List[Task] = []
        self.filename = Path(filename)

        # if the task file already exists, try and parse it
        if self.filename.exists():
            self.parse()

    def parse(self) -> None:
        self.tasks = self._parse_task_file(self.filename)

    def save(self) -> None:
        self._save_task_file(self.tasks, self.filename)

    @staticmethod
    def _parse_task_file(task_file: Path) -> List[Task]:
        tasks: List[Task] = []

        # First parse the yaml
        with task_file.open() as task_fh:
            yaml_tasks = yaml.load(task_fh, Loader=yaml.FullLoader)

        # Then validate the tasks
        for cur_yaml in yaml_tasks:
            try:
                cur_task = Task(**cur_yaml)
                tasks.append(cur_task)
            except ValidationError as e:
                print(e)

        return tasks

    @staticmethod
    def _save_task_file(tasks: List[Task], task_file: Path) -> None:
        with task_file.open('w') as task_fh:
            yaml.dump(tasks, task_fh)
