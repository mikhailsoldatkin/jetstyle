# Generated by Django 5.0.4 on 2024-04-23 13:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FibonacciTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('STARTED', 'Started'), ('SUCCESS', 'Success'), ('FAILURE', 'Failure')], default='PENDING', max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_done', models.DateTimeField(blank=True, null=True)),
                ('level', models.PositiveIntegerField()),
                ('result', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
