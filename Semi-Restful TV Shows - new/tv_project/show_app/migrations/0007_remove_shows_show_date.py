# Generated by Django 2.2.4 on 2023-06-08 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_app', '0006_auto_20230608_0603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shows',
            name='show_date',
        ),
    ]
