# Generated by Django 5.0.1 on 2024-02-10 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 11, 2, 38, 31, 2196)),
        ),
    ]
