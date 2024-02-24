from django.urls import path
from .views import *

urlpatterns = [
    path("operator_token/", OperatorTokenAPIView.as_view()),
    path("driver_token/", DriverTokenAPIView.as_view()),
]
