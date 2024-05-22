from django.test import TestCase
from django.urls import reverse
from todo_list.models import Task, Tag
from django.utils import timezone


class TaskViewsTests(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name="tag1")
        self.task = Task.objects.create(content="Test Task", deadline=timezone.now())

    def test_index_view(self):
        response = self.client.get(reverse("todo_list:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo_list/index.html")

    def test_task_create_view(self):
        response = self.client.post(
            reverse("todo_list:task-create"),
            {"content": "New Task", "deadline": timezone.now(), "tags": [self.tag.id]},
        )
        self.assertEqual(response.status_code, 302)  # Redirects after success
        self.assertTrue(Task.objects.filter(content="New Task").exists())

    def test_task_update_view(self):
        response = self.client.post(
            reverse("todo_list:task-update", args=[self.task.id]),
            {
                "content": "Updated Task",
                "deadline": self.task.deadline,
                "tags": [self.tag.id],
            },
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.content, "Updated Task")

    def test_task_delete_view(self):
        response = self.client.post(
            reverse("todo_list:task-delete", args=[self.task.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_toggle_task_status(self):
        response = self.client.post(
            reverse("todo_list:toggle_task_status", args=[self.task.id])
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.done)
