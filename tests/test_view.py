from django.test import TestCase
from django.urls import reverse

from wood.models import Task, Tags

TASK_URL = reverse("wood:task-list")
TAGS_URL = reverse("wood:tags-list")
STATUS_URL = reverse("wood:task-status", args=[1, 1])


class PublicTests(TestCase):
    def test_retrieve_tags(self):
        Tags.objects.create(
            name="test1",
        )

        response = self.client.get(TAGS_URL)
        tags = Tags.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["tags_list"]),
            list(tags)
        )

    def test_retrieve_task(self):
        tags_test = Tags.objects.create(
            name="test1",
        )

        task_tst = Task.objects.create(
            content="test2",
            status=True,
        )
        task_tst.tags.add(tags_test)

        response = self.client.get(TASK_URL)
        task = Task.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(task)
        )

    def test_task_str_model(self):
        task_test = Task.objects.create(
            content="test2",
            status=True,
        )

        self.assertEqual(
            str(task_test),
            task_test.content
        )

    def test_create_task(self):
        content = "test2",
        tags_test = Tags.objects.create(
            name="test1",
        )
        task = Task.objects.create(
            content=content,
            status=True,
        )
        task.tags.add(tags_test)

        self.assertEqual(task.content, content)
        self.assertEqual(task.status, True)

    def test_task_cheng_status(self):
        tags_test = Tags.objects.create(
            name="test1",
        )
        task = Task.objects.create(
            content="test2",
            status=False,
        )
        task.tags.add(tags_test)
        response = self.client.get(STATUS_URL)
        self.assertEqual(
            response.context["task_list"].get(pk=1).status,
            True
        )


