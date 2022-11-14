from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255, unique=True)
    created_date = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    class Meta:
        ordering = ["status", "created_date"]

    def __str__(self):
        return f"{self.content} ({self.status}, {self.tags}, {self.created_date})"
