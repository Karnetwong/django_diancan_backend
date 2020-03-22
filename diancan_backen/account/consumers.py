import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'ops_coffee'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(type(text_data_json),4)
        message = text_data_json['message']
        print(message,4444)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = '新订单提醒'
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
        }))

from channels.layers import get_channel_layer
def push():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'ops_coffee',
        {
            "type":"chat.message",
        }
    )