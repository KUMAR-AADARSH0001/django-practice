from channels.consumer import AsyncConsumer


class MyAsyncConsumer(AsyncConsumer):
    """
    this handler is called when client initialy opens a
    connection and is about to finish the websocket handsake
    """
    async def websocket_connect(seef, event):
        print('Websocket Connected')

    """
    this handler is called when data recieve from client
    """
    async def websocket_recieve(seef, event):
        print('Websocket Recieved')

    """
    this handler is called when connection and client is lost
    """
    async def websocket_disconnect(seef, event):
        print('Websocket Disconnected')
