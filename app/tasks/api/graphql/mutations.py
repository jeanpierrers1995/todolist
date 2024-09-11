"""
    This file contains the mutations for the tasks app.
"""

import strawberry
from app.tasks.models import Task
from .queries import TaskType
from django.core.exceptions import ObjectDoesNotExist


@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_task(self, title: str, description: str, completed: bool) -> TaskType:
        task = Task.objects.create(title=title, description=description, completed=completed)
        return TaskType(id=task.id, title=task.title, description=task.description, completed=task.completed)

    @strawberry.mutation
    def update_task(self, id: int, title: str, description: str, completed: bool) -> TaskType:
        try:
            task = Task.objects.get(id=id)
            task.title = title
            task.description = description
            task.completed = completed
            task.save()
            return TaskType(id=task.id, title=task.title, description=task.description, completed=task.completed)
        except ObjectDoesNotExist:
            raise Exception(f"Task with ID {id} not found.")

    @strawberry.mutation
    def delete_task(self, id: int) -> str:
        try:
            task = Task.objects.get(id=id)
            task.delete()
            return f"Task with ID {id} was deleted."
        except ObjectDoesNotExist:
            raise Exception(f"Task with ID {id} not found.")
