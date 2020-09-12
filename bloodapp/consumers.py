import asyncio
import json  
#from channels.consumer import AsyncConsumer

from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from channels.generic.websocket import JsonWebsocketConsumer
from django.db.models.signals import post_save
from django.dispatch import receiver
from bloodrequestapp.models import BloodRequest
from bloodrequestapp.models import UserGroup, BloodRequest, Membership

class NotifyConsumer(JsonWebsocketConsumer):

    
    def connect(self):
        
        user = self.scope['user']
        latest_req_instance = self.get_current_request(user)
        self.broadcast_group = 'request_{}'.format(latest_req_instance.id)
        #print(f'in connect {self.broadcast_group}')
        async_to_sync(self.channel_layer.group_add)(
            "gossip",
            self.channel_name
        )
        self.accept()

    def receive_json(self, content, **kwargs):
        print(f'Received event: {content}')
        
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            "gossip",
            self.channel_name
        )
    
    def send_request(self, event):
        print("message:", event['data'])
        self.send_json(event['data'])

    def get_current_request(self, user):
        return BloodRequest.objects.filter(sender=user).latest()

    @staticmethod
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
        
            if possible_list_of_donors is not None:
                for group in all_groups:
                    if group.group_code in possible_list_of_donors:
                        blood_group = group.group_name
                        group.request.add(instance)
                        
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "gossip", {
                    "type": "send.request",
                    "data": "Hello world"
                }
            )

    
     
    
