import asyncio
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class NoseyConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(
            'gossip',
            self.channel_layer
            )