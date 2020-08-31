from django.shortcuts import render, redirect
from .models import UserGroup, Membership
from bloodapp.models import User, Profile, BloodRequest
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse

