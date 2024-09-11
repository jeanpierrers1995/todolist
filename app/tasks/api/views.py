from rest_framework import generics
from rest_framework.exceptions import NotFound

from app.tasks.models import Task

from .serializers import TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve list of tasks or create new task.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete task.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_object(self):
        """
        Retrieve and return the task instance.
        Raises a 404 NotFound exception if the task does not exist.
        """
        try:
            return super().get_object()
        except Task.DoesNotExist:
            raise NotFound(detail="Error: Task not found.", code=404)
