from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('GenericViewSet1.urls')),
    path('api/v1/', include('GenericViewSet2.urls')),
    path('api/v1/', include('GenericViewSet3.urls')),
    path('api/v1/', include('GenericViewSet4.urls')),
    path('api/v1/', include('GenericViewSet5.urls')),
]
