import json
from channels.generic.websocket import AsyncWebsocketConsumer

from asgiref.sync import sync_to_async

from .models import CryptoData


class UpdatePriceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'price'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        # await self.send(text_data='TESTING')

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'update_price',
                'payload': text_data
            }
        )

    async def update_price(self, event):
        data = json.loads(event['price'])
        await self.send(text_data=json.dumps({
            'payload': data
        }))
