# Generated by Django 2.2.4 on 2023-06-07 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_app', '0003_auto_20230607_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='desc',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='shows',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 7, 17, 23, 11, 871750)),
        ),
        migrations.AlterField(
            model_name='shows',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 7, 17, 23, 11, 871750)),
        ),
    ]