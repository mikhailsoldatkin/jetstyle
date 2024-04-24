import uuid

from django.db import models


class FibonacciTask(models.Model):
    """Модель Задача расчета числа Фибоначчи."""

    PENDING = 'PENDING'
    STARTED = 'STARTED'
    SUCCESS = 'SUCCESS'
    FAILURE = 'FAILURE'

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (STARTED, 'Started'),
        (SUCCESS, 'Success'),
        (FAILURE, 'Failure'),
    )

    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_done = models.DateTimeField(null=True, blank=True)
    level = models.PositiveIntegerField()
    result = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('date_created',)
