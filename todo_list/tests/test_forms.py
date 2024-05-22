from django.test import TestCase
from todo_list.forms import TaskForm
from todo_list.models import Tag, Task
from django.utils import timezone


class TaskFormTests(TestCase):

    def setUp(self):
        self.tag1 = Tag.objects.create(name="tag1")
        self.tag2 = Tag.objects.create(name="tag2")

    def test_valid_form(self):
        data = {
            "content": "Test Task",
            "deadline": timezone.now(),
            "done": False,
            "tags": [self.tag1.id, self.tag2.id],
        }
        form = TaskForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            "content": "",
            "deadline": timezone.now(),
            "done": False,
            "tags": [self.tag1.id, self.tag2.id],
        }
        form = TaskForm(data=data)
        self.assertFalse(form.is_valid())
