from .models import User, Profile
from bloodrequestapp.models import Membership, UserGroup, BloodRequest
from allauth.account.signals import user_signed_up
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


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
		created = Profile.objects.get_or_create(user=instance, address=address, blood_group=group)[1]
		member = Membership.objects.create(individual=instance, group=group)
		member.save()
		print(created)


@receiver(post_save, sender=BloodRequest)
def announce_new_request(sender, instance, created, **kwargs):
	if created:
		channel_layer = get_channel_layer()

		'''
			sending messsage through the channel layer inform of a broadcast.
		'''
		async_to_sync(channel_layer.group_send)(
			"gossip", {
				"type": "user.gossip",
				"event": "New User",
				"username": instance.username 
			}
		)
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
