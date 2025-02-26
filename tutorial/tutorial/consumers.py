import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Carrera
class MyConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        carr = await self.getCarreras()
        data = [{'nombre':c.nombre, 'descripcion':c.descripcion} for c in carr]
        await self.send(text_data=json.dumps({
            'message': data
        }))
        
    async def disconnect(self, close_code):
        pass
    
    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            data = json.loads(text_data)
            nombre = data.get("nombre")
            descripcion = data.get("descripcion")

            if nombre and descripcion:
                await self.guardarCarrera(nombre, descripcion)

    @database_sync_to_async
    def guardarCarrera(self, nombre, descripcion):
        return Carrera.objects.create(nombre=nombre, descripcion=descripcion)
    @database_sync_to_async
    def getCarreras(self):
        return list(Carrera.objects.all().order_by('nombre'))