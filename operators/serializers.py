from rest_framework import serializers

from .models import *


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            "driver": {"required": False},
            "status": {"required": False},
            "grade": {"required": False},
            "waiting_seconds": {"required": False},
            "total_sum": {"required": False},
        }


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["driver", "total_sum", "status", "waiting_seconds"]
