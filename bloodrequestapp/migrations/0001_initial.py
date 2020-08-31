# Generated by Django 3.1 on 2020-08-30 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_joined', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
                ('group_code', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('O-', 'O-'), ('A-', 'A-'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=3)),
                ('group_slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('member', models.ManyToManyField(related_name='group_member', through='bloodrequestapp.Membership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='bloodrequestapp.usergroup'),
        ),
        migrations.AddField(
            model_name='membership',
            name='individual',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('request_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodrequestapp.usergroup', verbose_name='donor')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='receipient')),
            ],
        ),
    ]
