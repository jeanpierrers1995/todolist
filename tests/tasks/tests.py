import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from app.tasks.models import Task


@pytest.mark.django_db
def test_get_all_tasks():
    client = APIClient()
    url = reverse("task-list-create")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_task():
    client = APIClient()
    url = reverse("task-list-create")
    data = {
        "title": "New Task Crehana",
        "description": "Description Crehana",
        "completed": False,
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["title"] == "New Task Crehana"


@pytest.mark.django_db
def test_get_task_by_id():
    client = APIClient()
    task = Task.objects.create(
        title="Sample Task", description="Sample", completed=False
    )
    url = reverse("task-detail", args=[task.id])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == task.title


@pytest.mark.django_db
def test_update_task():
    client = APIClient()
    task = Task.objects.create(
        title="Task to Update", description="Sample", completed=False
    )
    url = reverse("task-detail", args=[task.id])
    data = {
        "title": "Updated Task",
        "description": "Updated description",
        "completed": True,
    }
    response = client.put(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == "Updated Task"
    assert response.data["completed"] is True


@pytest.mark.django_db
def test_delete_task():
    client = APIClient()
    task = Task.objects.create(
        title="Task to Delete", description="Sample", completed=False
    )
    url = reverse("task-detail", args=[task.id])
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Task.objects.filter(id=task.id).count() == 0
