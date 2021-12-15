from django.db import models
from django.utils import timezone


class ToDO(models.Model):
    task = models.CharField(max_length = 200)
    complete = models.BooleanField(default = False)
    time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.task