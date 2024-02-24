from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *


class OrderCreateAPIView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(status="active")

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "order_group",
                {
                    "type": "add_new_order",
                },
            )

            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        orders = Order.objects.all()
        status = request.query_params.get("status")  # ?status=.......
        sana = request.query_params.get("sana")  # ?sana=.......
        if status:
            orders = orders.filter(status=status)
        if sana:
            orders = orders.filter(date_time__contains=sana)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderUpdateAPIView(APIView):
    def put(self, request, pk):
        order = Order.objects.get(id=pk)
        serializer = OrderUpdateSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save(
                status=serializer.validated_data.get("status"),
                driver=serializer.validated_data.get("driver"),
                total_sum=serializer.validated_data.get("total_sum"),
                waiting_seconds=serializer.validated_data.get("waiting_seconds"),
            )

            if serializer.data.get("status") == "yakunlandi":
                client = Client.objects.get(id=order.client.id)
                driver = Driver.objects.get(id=serializer.data.get("driver"))

                foiz = driver.category.bonus_percent
                summa = (foiz * serializer.data.get("total_sum")) // 100
                client.total_bonus += summa
                client.save()

                foiz = driver.category.firm_percent
                summa = (foiz * serializer.data.get("total_sum")) // 100
                driver.balance = driver.balance - summa if (driver.balance - summa) >= 0 else 0
                driver.save()

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "order_group",
                {
                    "type": "add_new_order",
                },
            )

            return Response(serializer.data)
        return Response(serializer.errors)
