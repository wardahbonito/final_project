# Generated by Django 5.1 on 2024-10-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peer', '0008_remove_event_student_id_fill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
