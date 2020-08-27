from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django_countries.fields import CountryField
from django.urls import reverse
from django.utils.text import slugify
import random
import string
from Bloodbank import settings
from bloodrequestapp.models import UserGroup


def _random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class User(AbstractUser):
    pass


class Profile(models.Model):

    GENDER = (('m','Male'), ('f','Female'))
    

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER)
    phone = models.CharField(max_length=11, blank=True, null=True)
    country = CountryField()
    address = models.TextField()
    image = models.ImageField(default='default.jpeg',   upload_to='profile_pics')
    blood_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} ({self.user.email})'


