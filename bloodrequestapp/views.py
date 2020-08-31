from django.shortcuts import render, redirect
from .models import UserGroup, Membership
from bloodapp.models import User, Profile, BloodRequest
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse

@login_required
def blood_donate(request):
    return render(request, 'bloodapp/donate.html')

@login_required
def blood_request(request):
    return render(request, 'bloodapp/request.html')

@login_required
def blood_refer(request):
    return render(request, 'bloodapp/refer.html')