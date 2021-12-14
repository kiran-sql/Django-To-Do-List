from django.db import models
from django.utils import timezone


class ToDO(models.Model):
    task = models.CharField(max_length = 200)
    details = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task