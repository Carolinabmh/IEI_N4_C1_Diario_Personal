from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from rest_framework import viewsets, serializers
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    SAFE_METHODS
)

from .models import Entrada, Categoria, Estado, HistorialEstado

from .serializer import (
    EntradaSerializer,
    CategoriaSerializer,
    EstadoSerializer,
    HistorialEstadoSerializer
)

from .forms import (
    EntradaForm,
    CategoriaForm,
    EstadoForm,
    HistorialEstadoForm
)


# ==========================================
# VISTAS BASADAS EN FUNCIONES (FBV)
# ==========================================

# Página pública de bienvenida
def inicio(request):
    return render(request, 'inicio.html')


# Página personalizada de error 404
def error_404(request, exception):
    return render(request, '404.html', status=404)


# ==========================================
# API REST - VIEWSETS
# ==========================================

# API REST de entradas
class EntradaViewSet(viewsets.ModelViewSet):
    serializer_class = EntradaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user

        if usuario.is_staff:
            return Entrada.objects.all()

        return Entrada.objects.filter(usuario=usuario)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


# API REST de categorías
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]

        return [IsAdminUser()]


# API REST de estados
class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]

        return [IsAdminUser()]


# API REST del historial de estados
class HistorialEstadoViewSet(viewsets.ModelViewSet):
    serializer_class = HistorialEstadoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user

        if usuario.is_staff:
            return HistorialEstado.objects.all()

        return HistorialEstado.objects.filter(
            entrada__usuario=usuario
        )

    def perform_create(self, serializer):
        entrada = serializer.validated_data['entrada']

        if not self.request.user.is_staff:
            if entrada.usuario_id != self.request.user.id:
                raise serializers.ValidationError(
                    "No puedes registrar cambios en una entrada de otro usuario."
                )

        serializer.save()

    def perform_update(self, serializer):
        entrada = serializer.validated_data.get(
            'entrada',
            serializer.instance.entrada
        )

        if not self.request.user.is_staff:
            if entrada.usuario_id != self.request.user.id:
                raise serializers.ValidationError(
                    "No puedes modificar el historial de otro usuario."
                )

        serializer.save()


# ==========================================
# PERMISOS PARA LAS VISTAS WEB
# ==========================================

# Permitir acceso solamente al administrador
class AdministradorMixin(
    LoginRequiredMixin,
    UserPassesTestMixin
):
    def test_func(self):
        return self.request.user.is_staff


# Filtrar las entradas según el usuario
class EntradaUsuarioMixin(LoginRequiredMixin):

    def get_queryset(self):
        usuario = self.request.user

        if usuario.is_staff:
            return Entrada.objects.all()

        return Entrada.objects.filter(usuario=usuario)


# Filtrar el historial según el usuario
class HistorialUsuarioMixin(LoginRequiredMixin):

    def get_queryset(self):
        usuario = self.request.user

        if usuario.is_staff:
            return HistorialEstado.objects.all()

        return HistorialEstado.objects.filter(
            entrada__usuario=usuario
        )


# ==========================================
# CRUD MANUAL DE ENTRADAS (CBV)
# ==========================================

# Listar entradas
class EntradaListView(EntradaUsuarioMixin, ListView):
    model = Entrada
    template_name = 'entradas/entrada/listado_entradas.html'
    context_object_name = 'entradas'


# Detalle de una entrada
class EntradaDetailView(EntradaUsuarioMixin, DetailView):
    model = Entrada
    template_name = 'entradas/entrada/detalle_entrada.html'
    context_object_name = 'entrada'


# Crear entrada
class EntradaCreateView(LoginRequiredMixin, CreateView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'entradas/entrada/formulario_entrada.html'
    success_url = reverse_lazy('listado_entradas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


# Modificar entrada
class EntradaUpdateView(EntradaUsuarioMixin, UpdateView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'entradas/entrada/formulario_entrada.html'
    success_url = reverse_lazy('listado_entradas')


# Eliminar entrada
class EntradaDeleteView(EntradaUsuarioMixin, DeleteView):
    model = Entrada
    template_name = 'entradas/entrada/eliminar_entrada.html'
    success_url = reverse_lazy('listado_entradas')


# ==========================================
# CRUD MANUAL DE CATEGORÍAS (CBV)
# ==========================================

# Listar categorías
class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'entradas/categoria/listado_categorias.html'
    context_object_name = 'categorias'


# Detalle de una categoría
class CategoriaDetailView(LoginRequiredMixin, DetailView):
    model = Categoria
    template_name = 'entradas/categoria/detalle_categoria.html'
    context_object_name = 'categoria'


# Crear categoría
class CategoriaCreateView(AdministradorMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'entradas/categoria/formulario_categoria.html'
    success_url = reverse_lazy('listado_categorias')


# Modificar categoría
class CategoriaUpdateView(AdministradorMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'entradas/categoria/formulario_categoria.html'
    success_url = reverse_lazy('listado_categorias')


# Eliminar categoría
class CategoriaDeleteView(AdministradorMixin, DeleteView):
    model = Categoria
    template_name = 'entradas/categoria/eliminar_categoria.html'
    success_url = reverse_lazy('listado_categorias')


# ==========================================
# CRUD MANUAL DE ESTADOS (CBV)
# ==========================================

# Listar estados
class EstadoListView(LoginRequiredMixin, ListView):
    model = Estado
    template_name = 'entradas/estado/listado_estados.html'
    context_object_name = 'estados'


# Detalle de un estado
class EstadoDetailView(LoginRequiredMixin, DetailView):
    model = Estado
    template_name = 'entradas/estado/detalle_estado.html'
    context_object_name = 'estado'


# Crear estado
class EstadoCreateView(AdministradorMixin, CreateView):
    model = Estado
    form_class = EstadoForm
    template_name = 'entradas/estado/formulario_estado.html'
    success_url = reverse_lazy('listado_estados')


# Modificar estado
class EstadoUpdateView(AdministradorMixin, UpdateView):
    model = Estado
    form_class = EstadoForm
    template_name = 'entradas/estado/formulario_estado.html'
    success_url = reverse_lazy('listado_estados')


# Eliminar estado
class EstadoDeleteView(AdministradorMixin, DeleteView):
    model = Estado
    template_name = 'entradas/estado/eliminar_estado.html'
    success_url = reverse_lazy('listado_estados')


# ==========================================
# CRUD MANUAL DEL HISTORIAL (CBV)
# ==========================================

# Listar historial
class HistorialEstadoListView(
    HistorialUsuarioMixin,
    ListView
):
    model = HistorialEstado
    template_name = 'entradas/historial/listado_historial.html'
    context_object_name = 'historiales'


# Detalle del historial
class HistorialEstadoDetailView(
    HistorialUsuarioMixin,
    DetailView
):
    model = HistorialEstado
    template_name = 'entradas/historial/detalle_historial.html'
    context_object_name = 'historial'


# Crear historial
class HistorialEstadoCreateView(
    LoginRequiredMixin,
    CreateView
):
    model = HistorialEstado
    form_class = HistorialEstadoForm
    template_name = 'entradas/historial/formulario_historial.html'
    success_url = reverse_lazy('listado_historial')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['usuario'] = self.request.user
        return kwargs


# Modificar historial
class HistorialEstadoUpdateView(
    HistorialUsuarioMixin,
    UpdateView
):
    model = HistorialEstado
    form_class = HistorialEstadoForm
    template_name = 'entradas/historial/formulario_historial.html'
    success_url = reverse_lazy('listado_historial')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['usuario'] = self.request.user
        return kwargs


# Eliminar historial
class HistorialEstadoDeleteView(
    HistorialUsuarioMixin,
    DeleteView
):
    model = HistorialEstado
    template_name = 'entradas/historial/eliminar_historial.html'
    success_url = reverse_lazy('listado_historial')
