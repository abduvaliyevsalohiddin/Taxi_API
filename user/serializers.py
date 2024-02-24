from rest_framework import serializers

from .models import *


class CustomDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["username"]


class CustomerOperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["username", "password"]
