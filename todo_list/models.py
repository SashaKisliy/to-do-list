from django.db import models


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ["done", "-created_at"]

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
