from django.contrib import admin
from .models import User, Profile
from bloodrequestapp.models import BloodRequest

#from .bloodrequestmodels import BloodRequest
# Register your models here.

class RequestInline(admin.TabularInline):
	model = BloodRequest
	extra = 1

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

	inlines = [
		RequestInline,
	]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	pass

