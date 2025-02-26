from django.urls import path
from .consumers import MyConsumer

websocket_urlpatterns = [
    path('ws/test/', MyConsumer.as_asgi()),
]