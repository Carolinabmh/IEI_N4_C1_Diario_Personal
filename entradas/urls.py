from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'entradas', views.EntradaViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'estados', views.EstadoViewSet)
router.register(r'historial-estados', views.HistorialEstadoViewSet)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('api/', include(router.urls)),
]