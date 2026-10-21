from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import MiUsuario
from .serializer import MiUsuarioSerializer


class MiUsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MiUsuario.objects.all()
    serializer_class = MiUsuarioSerializer
    permission_classes = [IsAdminUser]

#ReadOnlyModeViewset permite consultar el listado de usuarios y obtener sus detalles por ID
#IsAdminUser restrige el acceso a usuarios con permisos de administrados