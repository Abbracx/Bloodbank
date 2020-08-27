from django.shortcuts import render, redirect
from .models import User, Profile
from bloodrequestapp.models import Membership, UserGroup, BloodRequest
from django.urls import reverse
from .forms import UserUpdateForm, ProfileUpdateForm, ContactUsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse

@login_required
def homepage(request):
	
	form = ContactUsForm()
	return render(request, 'homepage.html', {'form': form})

@login_required
def profile(request, user_id):
	
	context = {}

	try:
		user = User.objects.get(pk=user_id)
	except User.DoesNotExist:
		return HttpResponse('no user')

	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST or None, instance=user)
		profile_form = ProfileUpdateForm(request.POST or None, request.FILES, instance=user.profile)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, f'profile updated successfuly')
			return redirect('bloodapp:profile', user_id)
		else:
			user_form = UserUpdateForm(instance=user)
			profile_form = ProfileUpdateForm(instance=user.profile)
			
	user_form = UserUpdateForm(instance=user)
	profile_form = ProfileUpdateForm(instance=user.profile)

	context = {'user': user, 'profile_form': profile_form, 'user_form': user_form}
	return render(request, 'bloodapp/profile.html', context)
	

def about(request):
	return HttpResponse('These is about page.')
	#return render(request, 'bloodapp/profile.html', context)


def contact_us(request):

	if request.method == 'POST':
		form = ContactUsForm(request.POST)
		if form.is_valid():
			
			name = form.cleaned_data['name']
			sender = form.cleaned_data['email']
			message = form.cleaned_data['message']
			subject = '{} contact us on blood app.'.format(name)
			recipients = ['tankoraphael@gmail.com']

			send_mail(subject, message, sender, recipients)
			messages.success(request, f'message sent successfully.')
			return redirect('bloodapp:homepage')
		else:
			messages.error(request, f'Bad request, resend message.')
			return redirect('bloodapp:homepage')
	else:
		form = ContactUsForm()
	return render(request, 'homepage.html', {'form': form})