from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
