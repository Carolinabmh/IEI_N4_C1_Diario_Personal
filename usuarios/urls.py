from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


# Rutas de la API REST
router = DefaultRouter()
router.register(
    r'usuarios',
    views.MiUsuarioViewSet,
    basename='usuarios'
)


urlpatterns = [

    # API REST
    path('api/', include(router.urls)),

    # CRUD de usuarios
    path('usuarios/',
         views.MiUsuarioListView.as_view(),
         name='listado_usuarios'),

    path('usuarios/crear/',
         views.MiUsuarioCreateView.as_view(),
         name='crear_usuario'),

    path('usuarios/<int:pk>/',
         views.MiUsuarioDetailView.as_view(),
         name='detalle_usuario'),

    path('usuarios/<int:pk>/editar/',
         views.MiUsuarioUpdateView.as_view(),
         name='editar_usuario'),

    path('usuarios/<int:pk>/eliminar/',
         views.MiUsuarioDeleteView.as_view(),
         name='eliminar_usuario'),

    # Autenticación
    path('login/',
         views.IniciarSesionView.as_view(),
         name='login'),

    path('logout/',
         views.CerrarSesionView.as_view(),
         name='logout'),

    path('registro/',
         views.RegistroUsuarioView.as_view(),
         name='registro'),
]