import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import MyNum


class MyConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type": "websocket.accept"
        })
        '''
        await asyncio.sleep(2)
        await self.send({
            "type": "websocket.send",
            "text": "Hello world"
        })
        '''

    async def websocket_receive(self, event):
        print("receive", event)
        recv_msg = event.get('text', None)
        recv_dict = json.loads(recv_msg)
        recv_text = recv_dict.get('text')
        print(recv_text)

        if recv_text is not None:
            print('save')
            await self.save_text(recv_text)
        else:
            print('get')
            txt = await self.get_text()
            await self.send({
                "type": "websocket.send",
                "text": txt
            })

    async def websocket_disconnect(self, event):
        print("disconnect", event)

    @database_sync_to_async
    def save_text(self, txt):
        try:
            obj = MyNum.objects.get(k=1)
        except MyNum.DoesNotExist:
            obj = MyNum(k=1)
            obj.save()
        
        obj.text = txt
        obj.save()

    @database_sync_to_async
    def get_text(self):
        try:
            obj = MyNum.objects.get(k=1)
        except MyNum.DoesNotExist:
            obj = MyNum(k=1)
            obj.save()

        return obj.text