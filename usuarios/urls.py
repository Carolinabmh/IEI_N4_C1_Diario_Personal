from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MiUsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', MiUsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
]

#DefaultRouter genera automaticamente dos rutas para consultar los usuarios

