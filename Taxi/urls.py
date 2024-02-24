from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Taxi API uchun swagger",
        default_version="V1",
        description="Taxi API",
        contact=openapi.Contact("Abduvaliyev Salohiddin. Email: abduvaliyevsalohiddin568@gmail.com")
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('drivers/', include("drivers.urls")),
    path('operators/', include("operators.urls")),
    path('payments/', include("payments.urls")),
    path('user/', include("user.urls")),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),

]
