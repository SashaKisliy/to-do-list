from django.test import TestCase
from django.utils import timezone
from todo_list.models import Task, Tag


class TaskModelTests(TestCase):

    def setUp(self):
        self.tag1 = Tag.objects.create(name="tag1")
        self.tag2 = Tag.objects.create(name="tag2")
        self.task = Task.objects.create(content="Test Task", deadline=timezone.now())

    def test_task_creation(self):
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.content, "Test Task")
        self.assertFalse(task.done)

    def test_task_str(self):
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(str(task), "Test Task")

    def test_task_ordering(self):
        task2 = Task.objects.create(
            content="Another Task", deadline=timezone.now(), done=True
        )
        tasks = Task.objects.all()
        self.assertEqual(tasks[0], self.task)
        self.assertEqual(tasks[1], task2)

    def test_tag_str(self):
        tag = Tag.objects.get(id=self.tag1.id)
        self.assertEqual(str(tag), "tag1")

    def test_task_tags(self):
        self.task.tags.add(self.tag1, self.tag2)
        self.assertEqual(self.task.tags.count(), 2)
