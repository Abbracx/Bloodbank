from .models import User, Profile, Membership, Group
from allauth.account.signals import user_signed_up
from django.dispatch import receiver


@receiver(user_signed_up)
def create_user_profile(sender, **kwargs):
	instance = kwargs['user']
	import pdb; pdb.set_trace()
	phone = kwargs['request'].POST.get('phone')
	created = Profile.objects.get_or_create(user=instance, phone=phone)[1]
	print(created)

'''
@receiver(user_signed_up)
def create_user_membership(sender, **kwargs):
	instance = kwargs['user']
	phone = kwargs['request'].POST.get('phone')
	try:
		user_obj = User.objects.get(pk=)
	created = Membership.objects.get_or_create(user=instance, phone=phone)[1]
	print(created)

'''
