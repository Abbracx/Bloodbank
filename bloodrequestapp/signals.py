from .models import Membership, UserGroup, BloodRequest
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
'''
def send_request(event):
    print("message:", event)

@receiver(post_save, sender=BloodRequest)
def announce_new_request(sender, instance, created, **kwargs):

    group_of_donors = {   
        #patient: [list_of_posible_donors]
        "A+" :  ['O-', 'O+', 'A-', 'A+'],
        "B+" :  ['O-', 'O+', 'B-', 'B+'],
        "AB+":  ['O-','O+','B-','B+','A-','A+','AB-','AB+'],
        "O+" :  ['O+','O-'],
        "O-" :  ['O-'],
        "AB-":  ['O-','B-', 'A-', 'AB-'],
        "B-" :  ['O+','B-'],
        "A-" :  ['O+','A-']
        }

    if created:

        possible_list_of_donors = group_of_donors.get(instance.blood_type, None)

        all_groups = UserGroup.objects.all()
        broadcast_group = 'request_{}'.format(instance.id)
        #import pdb; pdb.set_trace()
        if possible_list_of_donors is not None:
            for group in all_groups:
                if group.group_code in possible_list_of_donors:
                    blood_group = group.group_name
                    group.request.add(instance)

                    #sending messsage through the channel layer inform of a broadcast.
                    #create a chat room with respect to the request id
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            broadcast_group, {
                "type": "send.request",
                "message": "Hello world"
            }
        )
		
		#"event": "BLOOD REQUEST",
        #"sender": instance.sender 
		
'''