"""
ASGI config for tutorial project.
¿que es asgi?

ASGI es un protocolo de intercambio de aplicaciones web para aplicaciones web basadas en Python.
que es son las siglas asgi?


It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial.settings')
django.setup()
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from .router_socket import websocket_urlpatterns



django_asgi_app = get_asgi_application()

# esta es la llamada al ASGI callable
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(websocket_urlpatterns),
})