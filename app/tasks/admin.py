# Crear el admin para mi model Task
from django.contrib import admin
from .models import Task

admin.site.register(Task)
