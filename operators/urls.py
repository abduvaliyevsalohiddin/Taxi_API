from django.urls import path
from .views import *

urlpatterns = [
    path("order_create/", OrderCreateAPIView.as_view()),
    path("order_update/<int:pk>/", OrderUpdateAPIView.as_view()),
]
