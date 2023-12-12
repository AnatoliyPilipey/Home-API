from django.test import TestCase
from django.urls import reverse

from wood.models import Task, Tags

TASK_URL = reverse("wood:task-list")
TAGS_URL = reverse("wood:tags-list")


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
