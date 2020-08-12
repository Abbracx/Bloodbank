from django.contrib import admin
from .models import User, Profile, Member, Group, Request

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	pass


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
	pass

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
	pass

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
	pass