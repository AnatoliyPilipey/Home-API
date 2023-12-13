from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=90)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    date_task_created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    status = models.BooleanField()
    tags = models.ManyToManyField(Tags, related_name="tag")

    class Meta:
        ordering = ["-date_task_created"]

    def __str__(self):
        return self.content
