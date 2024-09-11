"""
    Contains all the queries for the tasks app
"""

import strawberry
from typing import List
from app.tasks.models import Task
from strawberry.types import Info


@strawberry.type
class TaskType:
    id: int
    title: str
    description: str
    completed: bool


@strawberry.type
class Query:
    @strawberry.field
    def all_tasks(self, info: Info) -> List[TaskType]:
        tasks = Task.objects.all()
        return [
            TaskType(
                id=task.id,
                title=task.title,
                description=task.description,
                completed=task.completed,
            )
            for task in tasks
        ]
