from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


# ==========================================
# ROUTER PARA LA API REST
# ==========================================

router = DefaultRouter()

router.register(
    r'entradas',
    views.EntradaViewSet,
    basename='entrada'
)

router.register(
    r'categorias',
    views.CategoriaViewSet
)

router.register(
    r'estados',
    views.EstadoViewSet
)

router.register(
    r'historial-estados',
    views.HistorialEstadoViewSet,
    basename='historial-estado'
)


urlpatterns = [

    # Página pública de bienvenida
    path('', views.inicio, name='inicio'),

    # API REST
    path('api/', include(router.urls)),


    # ==========================================
    # CRUD DE ENTRADAS
    # ==========================================

    path(
        'entradas/',
        views.EntradaListView.as_view(),
        name='listado_entradas'
    ),

    path(
        'entradas/crear/',
        views.EntradaCreateView.as_view(),
        name='crear_entrada'
    ),

    path(
        'entradas/<int:pk>/',
        views.EntradaDetailView.as_view(),
        name='detalle_entrada'
    ),

    path(
        'entradas/<int:pk>/editar/',
        views.EntradaUpdateView.as_view(),
        name='editar_entrada'
    ),

    path(
        'entradas/<int:pk>/eliminar/',
        views.EntradaDeleteView.as_view(),
        name='eliminar_entrada'
    ),


    # ==========================================
    # CRUD DE CATEGORÍAS
    # ==========================================

    path(
        'categorias/',
        views.CategoriaListView.as_view(),
        name='listado_categorias'
    ),

    path(
        'categorias/crear/',
        views.CategoriaCreateView.as_view(),
        name='crear_categoria'
    ),

    path(
        'categorias/<int:pk>/',
        views.CategoriaDetailView.as_view(),
        name='detalle_categoria'
    ),

    path(
        'categorias/<int:pk>/editar/',
        views.CategoriaUpdateView.as_view(),
        name='editar_categoria'
    ),

    path(
        'categorias/<int:pk>/eliminar/',
        views.CategoriaDeleteView.as_view(),
        name='eliminar_categoria'
    ),


    # ==========================================
    # CRUD DE ESTADOS
    # ==========================================

    path(
        'estados/',
        views.EstadoListView.as_view(),
        name='listado_estados'
    ),

    path(
        'estados/crear/',
        views.EstadoCreateView.as_view(),
        name='crear_estado'
    ),

    path(
        'estados/<int:pk>/',
        views.EstadoDetailView.as_view(),
        name='detalle_estado'
    ),

    path(
        'estados/<int:pk>/editar/',
        views.EstadoUpdateView.as_view(),
        name='editar_estado'
    ),

    path(
        'estados/<int:pk>/eliminar/',
        views.EstadoDeleteView.as_view(),
        name='eliminar_estado'
    ),


    # ==========================================
    # CRUD DEL HISTORIAL DE ESTADOS
    # ==========================================

    path(
        'historial/',
        views.HistorialEstadoListView.as_view(),
        name='listado_historial'
    ),

    path(
        'historial/crear/',
        views.HistorialEstadoCreateView.as_view(),
        name='crear_historial'
    ),

    path(
        'historial/<int:pk>/',
        views.HistorialEstadoDetailView.as_view(),
        name='detalle_historial'
    ),

    path(
        'historial/<int:pk>/editar/',
        views.HistorialEstadoUpdateView.as_view(),
        name='editar_historial'
    ),

    path(
        'historial/<int:pk>/eliminar/',
        views.HistorialEstadoDeleteView.as_view(),
        name='eliminar_historial'
    ),
]