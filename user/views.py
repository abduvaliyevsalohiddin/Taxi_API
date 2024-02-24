from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from .models import *


class OperatorTokenAPIView(APIView):
    @swagger_auto_schema(request_body=CustomDriverSerializer)
    def post(self, request):
        operator = Customer.objects.filter(
            username=request.data.get("username"),
            password=request.data.get("password"),
            role="operator"
        ).first()
        if operator is None:
            return Response({"xabar": "Operator topilmadi!"})
        refresh = RefreshToken().for_user(operator)
        resp = {
            "username": request.data.get("username"),
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }
        return Response(resp)


class DriverTokenAPIView(APIView):
    @swagger_auto_schema(request_body=CustomDriverSerializer)
    def post(self, request):
        driver = Customer.objects.filter(
            username=request.data.get("username"),
            role="driver"
        ).first()
        if driver is None:
            return Response({"xabar": "Haydovchi topilmadi!"})
        refresh = RefreshToken().for_user(driver)
        resp = {
            "username": request.data.get("username"),
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }
        return Response(resp)
