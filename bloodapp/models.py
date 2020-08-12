from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django_countries.fields import CountryField
from products.models import Product, Image, Category

class User(AbstractUser):
    

class Profile(models.Model):

    GENDER = (('m','Male'), ('f','Female'))
    

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER)
    phone = models.CharField(max_length=11, blank=True, null=True)
    blood_group = models.CharField()
    country = CountryField()
    address = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} ({self.user.email})'

class Membership(models.Model):

    individual  = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    group = models.ForeignKey(Group, on_delete=models.SET_DEFAULT)
    Date_joined = models.DateField(default=timezone.now)

class Group(models.Model):

    BLOOD_GROUP = (('A+','A+'), ('B+', 'B+'), ('O+', 'O+'))

    group_name = models.CharField(max_length=100, choices=BLOOD_GROUP)
    group_slug = models.SlugField(max_length=200, unique=True, blank=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE)

class Request(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='receipient')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='donor')
    message = models.CharField(max_length=255)
    request_date = models.DateTimeField(default=timezone.now)
    