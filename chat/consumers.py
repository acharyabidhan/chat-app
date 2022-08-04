import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'allInOne'
        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
        self.accept()
        self.send(text_data=json.dumps({"status":"connected"}))
    def receive(self, text_data=None, bytes_data=None):
        txt_data_msg = json.loads(text_data)
        async_to_sync(self.channel_layer.group_send)(self.group_name,{'type':'broadcast_all','data':txt_data_msg})
    def broadcast_all(self, e):
        msg = e['data']
        self.send(text_data=json.dumps(msg))