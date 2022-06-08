import json

from channels.generic.websocket import AsyncWebsocketConsumer # The class we're using
from asgiref.sync import sync_to_async # Implement later
from bulletin_board.models import Users as User

# Import the Message model
from .models import ChatModel


# Create a consumer cass
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        my_slug = self.scope['user'].slug
        other_slug = self.scope['url_route']['kwargs']['room_name']
        if my_slug > other_slug:
            self.room_name = f'{my_slug}-{other_slug}'
        else:
            self.room_name = f'{other_slug}-{my_slug}'

        # Join room based on name in the URL
        # self.room_name = self.scope['url_route']['kwargs']['room_name']

        self.room_group_name = 'chat_%s' % self.room_name

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

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']

        await self.save_message(username, self.room_group_name, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))

    @sync_to_async
    def save_message(self, username, thread_name, message):
        ChatModel.objects.create(sender=User.objects.get(username=username), message=message, thread_name=thread_name)