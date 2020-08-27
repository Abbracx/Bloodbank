from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django_countries.fields import CountryField
from django.urls import reverse
from django.utils.text import slugify
import random
import string
from Bloodbank import settings
from django.contrib.auth import get_user_model



def _random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class UserGroup(models.Model):

    BLOOD_GROUP = (('A+','A+'), ('B+', 'B+'),
                    ('O+', 'O+'),('O-','O-'),
                    ('A-','A-'),('B-','B-'),
                    ('AB+','AB+'),('AB-','AB-'))

    group_name = models.CharField(max_length=100)
    group_code = models.CharField(max_length=3, choices=BLOOD_GROUP)
    group_slug = models.SlugField(max_length=200, unique=True, blank=True)
    member= models.ManyToManyField(settings.AUTH_USER_MODEL, through='Membership', related_name='group_member')
    #request = models.ManyToManyField(BloodRequest,related_name ='group_request')

    def unique_slug_generator(self, new_slug=None):

        if new_slug is not None:
            slug = new_slug
        else:
            slug = slugify(self.group_name)
        
        Klass = self.__class__
        qs_exists  = Klass.objects.filter(group_slug=slug).exists()
        if qs_exists:
            new_slug = f'{slug}-{_random_string_generator(4)}'
            return self.unique_slug_generator(new_slug=new_slug)
        return slug

    def save(self, *args, **kwargs):
        self.group_slug = self.unique_slug_generator()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.group_code




class Membership(models.Model):

    individual  = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.SET_DEFAULT)
    group = models.ForeignKey(UserGroup, default=1, on_delete=models.SET_DEFAULT)
    Date_joined = models.DateField(default=timezone.now)

    def __str__(self):
        return  f'{Membership.objects.all().count()} members are available.'


class BloodRequest(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='receipient')
    receiver = models.ForeignKey(UserGroup, on_delete=models.CASCADE, verbose_name='donor')
    message = models.CharField(max_length=255)
    request_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.sender.username} sends a blood request to {self.receiver.group_name}'