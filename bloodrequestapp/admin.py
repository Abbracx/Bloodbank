from django.contrib import admin
from .models import Membership, UserGroup, BloodRequest
from django.apps import apps



@admin.register(BloodRequest)
class RequestAdmin(admin.ModelAdmin):
	pass

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
	list_display = ['individual', 'group', 'Date_joined']



class MembersInline(admin.TabularInline):
	model = Membership
	extra = 1


@admin.register(UserGroup)
class GroupAdmin(admin.ModelAdmin):
	list_display = ['group_code', 'group_name']
	ordering = ['group_code']
	filter_horizontal = ('request',)
	inlines = (MembersInline,)
	