from django import forms
from .models import User, Profile,  BloodRequest
from bloodrequestapp.models import Membership, UserGroup
from allauth.account.forms import SignupForm


class CustomSignUpForm(SignupForm):

    BLOOD_GROUP = (('A+','A+'), ('B+', 'B+'),
                    ('O+', 'O+'),('O-','O-'),
                    ('A-','A-'),('B-','B-'),
                    ('AB+','AB+'),('AB-','AB-'))

    blood_group = forms.CharField(max_length=5, widget=forms.Select(choices=BLOOD_GROUP), required=True)
    address = forms.CharField(max_length=200, widget=forms.Textarea, required=True)
    
    def signup(self, request, user):
        
        user.save()
        #user.profile.address = self.cleaned_data['address']
        #user.profile.save()

        return user

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields  =  ['phone','country','address','blood_group','image']

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        fields = ['name','email','message']