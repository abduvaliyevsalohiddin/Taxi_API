from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class DriversAPIView(APIView):
    def get(self, request):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DriverAPIViews(APIView):
    def put(self, request, pk):
        driver = Driver.objects.get(id=pk)
        serializer = DriverSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        Driver.objects.get(id=pk).delete()
        return Response({"success": " True", "message": "Tolov o`chirildi"})


class CarCategoryAPIView(APIView):
    def get(self, request):
        category = CarCategory.objects.all()
        serializer = CarCategorySerializer(category, many=True)
        return Response(serializer.data)
