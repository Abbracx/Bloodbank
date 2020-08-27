from django.contrib import admin
from .models import User, Profile
from bloodrequestapp.models import Membership, UserGroup, BloodRequest
#from .bloodrequestmodels import BloodRequest
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	pass


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
	list_display = ['individual', 'group', 'Date_joined']

@admin.register(UserGroup)
class GroupAdmin(admin.ModelAdmin):
	list_display = ['group_code', 'group_name']
	ordering = ['group_code']

@admin.register(BloodRequest)
class RequestAdmin(admin.ModelAdmin):
	pass