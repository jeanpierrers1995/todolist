from django.contrib import admin
from django.urls import include
from django.urls import path
from strawberry.django.views import GraphQLView

from app.tasks.api.graphql.schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("app.tasks.api.urls")),
    path("graphql/", GraphQLView.as_view(schema=schema)),
]
