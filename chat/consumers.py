import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'test'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({
            'type':"connection established",
            'msg':"hello world"
        }))
    
    def receive(self, text_data=None, bytes_data=None):
        txt_data_msg = json.loads(text_data)
        msg = txt_data_msg['msg']
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type':'chat_message',
                'msg':msg
            }
        )
    
    def chat_message(self, e):
        msg = e['msg']
        self.send(text_data=json.dumps({
            'type':'chat',
            'msg':msg
        }))