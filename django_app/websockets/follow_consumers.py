from channels.generic.websocket import AsyncWebsocketConsumer
import json


class FollowConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']   
        self.room_group_name = f'user_{self.user_id}_follows'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def send_follow_update(self, event):
        await self.send(text_data=json.dumps({
            'type': 'follow_update',
            'followers_count': event['followers_count'],
        }))
