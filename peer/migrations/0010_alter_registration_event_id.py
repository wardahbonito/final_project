# Generated by Django 5.1 on 2024-10-20 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peer', '0009_remove_event_id_alter_event_event_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peer.event'),
        ),
    ]
