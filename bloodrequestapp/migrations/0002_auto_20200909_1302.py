# Generated by Django 3.1 on 2020-09-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodrequestapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloodrequest',
            options={'get_latest_by': 'request_date'},
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='blood_type',
            field=models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('O-', 'O-'), ('A-', 'A-'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default=None, max_length=3),
        ),
    ]
