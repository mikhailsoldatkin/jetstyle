# from time import sleep

from celery import shared_task
from django.utils import timezone

from fibo.models import FibonacciTask


@shared_task
def fibonacci(n, uuid):
    """Вычисление ряда чисел Фибоначчи."""

    fibo_task = FibonacciTask.objects.get(uuid=uuid)
    fibo_task.status = FibonacciTask.STARTED
    fibo_task.save()

    fibo_sequence = []
    try:
        if n == 1:
            fibo_sequence = [0]
        elif n == 2:
            fibo_sequence = [0, 1]
        else:
            fibo_sequence = [0, 1]
            while len(fibo_sequence) < n:
                fibo_sequence.append(fibo_sequence[-1] + fibo_sequence[-2])
                # sleep(1)
            fibo_task.status = FibonacciTask.SUCCESS
            fibo_task.date_done = timezone.now()
    except Exception:
        fibo_task.status = FibonacciTask.FAILURE
    finally:
        fibo_task.save()

    return fibo_sequence
