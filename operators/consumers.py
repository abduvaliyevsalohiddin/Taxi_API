from channels.generic.websocket import AsyncWebsocketConsumer
from .models import *
from user.models import *
from .serializers import *
import json
from asgiref.sync import sync_to_async
from rest_framework_simplejwt.tokens import AccessToken


class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        token = self.scope.get("query_string").decode("utf-8")
        if token.startswith("token="):  # ws/orders/?token=sdjklfjohyj234hkj
            token = token.replace("token=", "")
            try:
                access_token = AccessToken(token)
                user_id = access_token['user_id']
                self.scope['user_id'] = user_id
            except Exception:
                await self.close()

        await self.accept()
        await self.channel_layer.group_add("order_group", self.channel_name)
        await self.send_initial_order_list()

    async def send_initial_order_list(self):
        user_id = self.scope['user_id']  # 15
        data = await self.get_user_data(user_id)  # 15
        order_list = await self.get_order_list(data)
        await self.send(text_data=json.dumps(order_list))

    @sync_to_async
    def get_order_list(self, data):
        order = Order.objects.filter(status='active')
        if data["role"] == 'driver':
            if data['data'].gender.lower() == 'erkak':
                order = order.exclude(for_women=True)
            if data['data'].has_baggage == False:
                order = order.exclude(baggage=True)
        serializer = OrderSerializer(order, many=True)
        return serializer.data

    @sync_to_async
    def get_user_data(self, pk):
        driver = Driver.objects.filter(id=pk).first()
        if driver:
            data = {"role": "driver", "data": driver}
        operator = Operator.objects.filter(id=pk).first()
        if operator:
            data = {"role": "operator", "data": operator}
        return data

    async def add_new_order(self, event):
        await self.send_initial_order_list()

    async def disconnect(self, code):
        await self.channel_layer.group_discard("order_group", self.channel_name)