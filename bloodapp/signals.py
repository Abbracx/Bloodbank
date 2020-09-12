from .models import User, Profile
from bloodrequestapp.models import Membership, UserGroup
from allauth.account.signals import user_signed_up
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(user_signed_up)
def create_user_profile(sender, request, **kwargs):
	instance = kwargs['user']
	#import pdb; pdb.set_trace()
	address = request.POST.get('address')
	blood_group = request.POST.get('blood_group')

	try:
		group = UserGroup.objects.filter(group_code=blood_group).first()
	except UserGroup.DoesNotExist:
		group = None
	else:
		Profile.objects.create(user=instance, address=address, blood_group=group)
		Membership.objects.create(individual=instance, group=group)
		group.members.add(instance)
		



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
