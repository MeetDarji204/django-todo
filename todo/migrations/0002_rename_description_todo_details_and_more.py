# Generated by Django 5.2.4 on 2025-07-17 20:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="description",
            new_name="details",
        ),
        migrations.RemoveField(
            model_name="todo",
            name="completed",
        ),
        migrations.RemoveField(
            model_name="todo",
            name="created_at",
        ),
        migrations.AddField(
            model_name="todo",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="todo",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
