from django.urls import re_path
from . import consumers

websocket_relpatterns = [
    re_path('ws/socket-server/', consumers.ChatConsumer.as_asgi())
]