# Generated by Django 4.1.3 on 2022-11-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_alter_task_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateField(blank=True, null=True),
        ),
    ]
