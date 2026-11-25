from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import MiUsuario
from .serializer import MiUsuarioSerializer
from .forms import MiUsuarioCreateForm, MiUsuarioUpdateForm


# API REST de usuarios
class MiUsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MiUsuario.objects.all()
    serializer_class = MiUsuarioSerializer
    permission_classes = [IsAdminUser]


# Permite el acceso solamente a administradores
class AdministradorMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser


# Listado de usuarios
class MiUsuarioListView(AdministradorMixin, ListView):
    model = MiUsuario
    template_name = 'usuarios/listado_usuarios.html'
    context_object_name = 'usuarios'


# Detalle de usuario
class MiUsuarioDetailView(AdministradorMixin, DetailView):
    model = MiUsuario
    template_name = 'usuarios/detalle_usuario.html'
    context_object_name = 'usuario'


# Crear usuario
class MiUsuarioCreateView(AdministradorMixin, CreateView):
    model = MiUsuario
    form_class = MiUsuarioCreateForm
    template_name = 'usuarios/formulario_usuario.html'
    success_url = reverse_lazy('listado_usuarios')


# Editar usuario
class MiUsuarioUpdateView(AdministradorMixin, UpdateView):
    model = MiUsuario
    form_class = MiUsuarioUpdateForm
    template_name = 'usuarios/formulario_usuario.html'
    success_url = reverse_lazy('listado_usuarios')

    def get_queryset(self):
        return MiUsuario.objects.filter(is_superuser=False)


# Eliminar usuario
class MiUsuarioDeleteView(AdministradorMixin, DeleteView):
    model = MiUsuario
    template_name = 'usuarios/eliminar_usuario.html'
    success_url = reverse_lazy('listado_usuarios')

    def get_queryset(self):
        return MiUsuario.objects.filter(
            is_superuser=False,
            is_staff=False
        )


# Inicio de sesión
class IniciarSesionView(LoginView):
    template_name = 'usuarios/login.html'


# Cierre de sesión
class CerrarSesionView(LogoutView):
    next_page = reverse_lazy('inicio')


# Registro de nuevos usuarios
class RegistroUsuarioView(CreateView):
    model = MiUsuario
    form_class = MiUsuarioCreateForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')