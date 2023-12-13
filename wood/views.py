from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm
from .models import Task, Tags


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("planwood:task-list")


class TaskStatusChangView(generic.ListView):
    model = Task

    def get_queryset(self):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        if self.kwargs["new"] == 1:
            task.status = True
            task.save()
        elif self.kwargs["new"] == 0:
            task.status = False
            task.save()
#        task.status.update(self.kwargs["new_status"])

        return Task.objects.all()


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("planwood:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("planwood:task-list")


class TagsListView(generic.ListView):
    model = Tags


class TagsCreateView(generic.CreateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("planwood:tags-list")


class TagsUpdateView(generic.UpdateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("planwood:tags-list")


class TagsDeleteView(generic.DeleteView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("planwood:tags-list")
