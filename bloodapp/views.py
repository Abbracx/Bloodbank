from django.shortcuts import render, redirect
from .models import User, Profile, Group, Membership, Request
from django.urls import reverse
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def homepage(request):
	return render(request, 'bloodapp/homepage.html')

@login_required
def profile(request, user_id):

	return render(request, 'bloodapp/profile.html', context)