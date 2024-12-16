import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name'] 
        self.room_group_name = f'chat_{self.room_name}'

        # join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        # leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        from django_app.models.message.message import Message
        from django_app.utils import get_user_model


        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender_username = text_data_json['sender']

        get_user = get_user_model()
        user = get_user.objects.get(username=sender_username)
        Message.objects.create(sender=user, room_name=self.room_name, content=message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender_username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # send message in chat room
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))
