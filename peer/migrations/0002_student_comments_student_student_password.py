# Generated by Django 5.1 on 2024-10-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comments',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='', max_length=100),
        ),
    ]
