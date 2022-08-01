from django.urls import re_path
from . import consumers

websocket_relpatterns = [
    re_path('chat-server/', consumers.ChatConsumer.as_asgi())
]