
from django.db import models


class Task(models.Model):
    TASK_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('in_progress', 'In Progress')
    ]
    task = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    task_status = models.CharField(
        max_length=50, choices=TASK_STATUS, default='pending'
    )

    def __str__(self):
        return self.task
