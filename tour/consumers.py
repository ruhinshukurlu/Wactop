import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer
from channels.exceptions import StopConsumer

class TestConsumer(AsyncJsonWebsocketConsumer):
    # groups = ["broadcast"]

    # def connect(self):
    #     # Called on connection.
    #     # To accept the connection call:
    #     self.accept()
    #     # Or accept the connection and specify a chosen subprotocol.
    #     # A list of subprotocols specified by the connecting client
    #     # will be available in self.scope['subprotocols']
    #     # self.accept("subprotocol")
    #     self.send(json.dumps({'test': 16}))
        # To reject the connection, call:
        # self.close()

    # def receive(self, text_data=None, bytes_data=None):
    #     # Called with either text_data or bytes_data for each frame
    #     # You can call:
    #     self.send(text_data="Hello world!")
    #     # Or, to send a binary frame:
    #     self.send(bytes_data="Hello world!")
    #     # Want to force-close the connection? Call:
    #     self.close()
    #     # Or add a custom WebSocket error code!
    #     self.close(code=4123)

    # def disconnect(self, close_code):
        # Called when the socket closes

    async def connect(self):
        await self.accept()
        # print("connected", event)
        self.story_id = self.scope['url_route']['kwargs']['pk']
        self.room = f'room_{self.story_id}'
        await self.channel_layer.group_add(
            self.room, # unique channel id
            self.channel_name # default attribute
        )
        print(f"Added {self.channel_name} channel to gossip")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room, # unique channel id
            self.channel_name # default attribute
        )
        print(f"Removed {self.channel_name} channel to gossip")

    async def send_message(self, event):
        message = event['text']

        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")

    # async def websocket_connect(self, event):
    #     print("connected", event)
    #     self.story_id = self.scope['url_route']['kwargs']['pk']
    #     self.room = f'room_{self.story_id}'
    #     await self.channel_layer.group_add(
    #         self.room, # unique channel id
    #         self.channel_name # default attribute
    #     )
        # await self.channel_layer.group_add("group_name", self.channel_name)

        # await self.send({
        #     'type':"websocket.accept",
        # })


        # await self.accept()


    # async def websocket_receive(self, event):
    #     print("receive", event)
    #     recived_data = json.loads(event.get('text'))
    #     comment_text = recived_data.get('text')
    #     user = self.scope['user']
    #     story = await self.get_story(self.story_id)
    #     parent_id = recived_data.get('parent_id')
    #     if parent_id != '':
    #         parent = await self.get_parent(int(parent_id))
    #         await self.create_comment(comment_text, user, story, parent)
    #     else:
    #         await self.create_comment(comment_text, user, story)
      
        # await self.channel_layer.group_send(
        #     self.room,
        #     {
        #         'type':'comment_message',
        #         'text':json.dumps(self.data_response),
        #     }
        # )

    # async def comment_message(self, event):
    #      await self.send({
    #         'type':'websocket.send',
    #         'text':event['text'],
    #     })

    # text_data=json.dumps({
    #         'message': message
    #     })
    # async def send_message(self, event):
    #     message = event['text']

    #     await self.send({
            
    #         'text': message
    #     })

    # async def websocket_disconnect(self, event):
    #     print('disconnected', event)
    #     await self.channel_layer.group_discard(
    #     self.room   ,
    #     self.channel_name
    #     )
    #     raise StopConsumer()
