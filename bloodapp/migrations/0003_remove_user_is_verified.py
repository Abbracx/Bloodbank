# Generated by Django 3.0.8 on 2020-08-13 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0002_auto_20200813_0600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_verified',
        ),
    ]
