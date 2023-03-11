from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print('Websocket Connected', event)
        self.send({
            'type': 'websocket.accept',
        })

    def websocket_recieve(self, event):
        print('Websocket Recieved', event)
        print('Message is ', event['text'])

    def websocket_disconnect(self, event):
        print('Websocket Disconnected', event)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print('Websocket Connected')
        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_recieve(self, event):
        print('Websocket Recieved')
        print('Message is ', event['text'])

    async def websocket_disconnect(self, event):
        print('Websocket Disconnected')
        raise StopConsumer()
