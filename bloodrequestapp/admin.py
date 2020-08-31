from django.contrib import admin
from .models import Membership, UserGroup


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
	list_display = ['individual', 'group', 'Date_joined']

@admin.register(UserGroup)
class GroupAdmin(admin.ModelAdmin):
	list_display = ['group_code', 'group_name']
	ordering = ['group_code']
