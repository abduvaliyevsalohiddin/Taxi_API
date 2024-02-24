from django.urls import path
from operators.consumers import *

websocket_urlpatterns = [
    path("ws/orders/", OrderConsumer.as_asgi()),
]
