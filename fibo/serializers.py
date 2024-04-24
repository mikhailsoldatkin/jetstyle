from celery.result import AsyncResult
from celery.states import SUCCESS
from rest_framework import serializers

from fibo.models import FibonacciTask


class LevelSerializer(serializers.Serializer):
    """Сериализатор параметра level для расчета числа Фибоначчи."""

    level = serializers.IntegerField(min_value=1)


class FibonacciTaskSerializer(serializers.ModelSerializer):
    """Сериализатор задачи."""

    elapsed_time = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    date_done = serializers.SerializerMethodField()
    result = serializers.SerializerMethodField()

    class Meta:
        model = FibonacciTask
        fields = (
            'uuid',
            'status',
            'date_created',
            'date_done',
            'elapsed_time',
            'level',
            'result',
        )

    def get_elapsed_time(self, obj):
        if obj.date_done and obj.date_created:
            elapsed = (obj.date_done - obj.date_created).total_seconds()
            return f'{elapsed:.2f} seconds'

    def get_date_created(self, obj):
        return obj.date_created.strftime('%Y-%m-%d %H:%M:%S')

    def get_date_done(self, obj):
        if obj.date_done:
            return obj.date_done.strftime('%Y-%m-%d %H:%M:%S')

    def get_result(self, obj):
        fibo_task = FibonacciTask.objects.get(uuid=obj.uuid)
        task = AsyncResult(obj.uuid)

        if task.status == SUCCESS:
            result = task.get()
            fibo_task.result = result
            fibo_task.save()

            return str(result)
