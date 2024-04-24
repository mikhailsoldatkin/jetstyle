from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from fibo.serializers import FibonacciTaskSerializer, LevelSerializer
from .models import FibonacciTask
from .tasks import fibonacci


class FibonacciTaskAPIView(APIView):
    """Создание и вывод списка задач по расчету числа Фибоначчи."""

    def post(self, request):
        serializer = LevelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        level = serializer.validated_data.get('level')

        fibo_task = FibonacciTask.objects.create(level=level)
        fibonacci.apply_async((level, fibo_task.uuid), task_id=str(fibo_task.uuid))

        return Response({f'message: task with level {level} added'}, status=status.HTTP_201_CREATED)

    def get(self, request):
        tasks = FibonacciTask.objects.all()
        serializer = FibonacciTaskSerializer(tasks, many=True)
        return Response(serializer.data)


class FibonacciTaskDetailAPIView(RetrieveAPIView):
    """Вывод информации о задаче по её идентификатору."""

    queryset = FibonacciTask.objects.all()
    serializer_class = FibonacciTaskSerializer
    lookup_field = 'uuid'
