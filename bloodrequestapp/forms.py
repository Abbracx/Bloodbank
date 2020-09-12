from django import forms
from bloodapp.models import User, Profile
from .models import UserGroup, Membership, BloodRequest




class BloodRequestForm(forms.ModelForm):
 
    class Meta:
        model = BloodRequest
        fields = ['blood_type','reason', 'message']
