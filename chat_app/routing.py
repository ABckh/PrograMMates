from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    # re_path(r'ws/chat/<str:room_name>', consumers.ChatConsumer),
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]