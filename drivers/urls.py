from django.urls import path
from .views import *

urlpatterns = [
    path("drivers/", DriversAPIView.as_view()),
    path("driver/<int:pk>/", DriverAPIViews.as_view()),
    path("category/", CarCategoryAPIView.as_view()),
]
