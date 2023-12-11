from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskStatusChangView,
    TagsListView,
    TagsCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagsUpdateView,
    TagsDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "task/<int:pk>/<int:new>",
        TaskStatusChangView.as_view(),
        name="task-status",
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path(
        "tags/create/",
        TagsCreateView.as_view(),
        name="tags-create",
    ),
    path(
        "tags/<int:pk>/update/",
        TagsUpdateView.as_view(),
        name="tags-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagsDeleteView.as_view(),
        name="tags-delete",
    ),
]

app_name = "wood"
