from django.db import models
from django.contrib.auth.models import User

str_habilitado = "Habilitado"
str_fecha_creacion = "Fecha Creación"
str_fecha_actualizacion = "Fecha Actualización"
str_nombre = "Nombre"
str_descripcion = "Descripción"


class Categoria(models.Model):
    nombre = models.CharField(str_nombre, max_length=50, null=False)
    descripcion = models.CharField(str_descripcion, max_length=100, null=True)

    habilitado = models.BooleanField(
        str_habilitado,
        default=True,
        null=False
    )

    created_at = models.DateTimeField(
        str_fecha_creacion,
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        str_fecha_actualizacion,
        auto_now=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        db_table_comment = "Categorías asociadas a las entradas del diario personal."


class Estado(models.Model):
    nombre = models.CharField(str_nombre, max_length=30, null=False)
    descripcion = models.CharField(str_descripcion, max_length=100, null=True)

    habilitado = models.BooleanField(
        str_habilitado,
        default=True,
        null=False
    )

    created_at = models.DateTimeField(
        str_fecha_creacion,
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        str_fecha_actualizacion,
        auto_now=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        db_table_comment = "Estados asociados a las entradas del diario personal."

class Entrada(models.Model):
    titulo = models.CharField("Título", max_length=100, null=False)
    contenido = models.TextField("Contenido", null=False)

    fecha_creacion = models.DateTimeField(
        str_fecha_creacion,
        auto_now_add=True
    )

    es_publica = models.BooleanField(
        "Es Pública",
        default=False
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE
    )

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    habilitado = models.BooleanField(
        str_habilitado,
        default=True,
        null=False
    )

    updated_at = models.DateTimeField(
        str_fecha_actualizacion,
        auto_now=True
    )

    def __str__(self):
        return self.titulo

    class Meta:
        db_table_comment = "Entradas registradas en el diario personal."


class HistorialEstado(models.Model):
    entrada = models.ForeignKey(
        Entrada,
        on_delete=models.CASCADE
    )

    estado_anterior = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        related_name='historial_anterior'
    )

    estado_nuevo = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        related_name='historial_nuevo'
    )

    fecha_cambio = models.DateTimeField(
        "Fecha Cambio",
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.entrada} - {self.estado_anterior} a {self.estado_nuevo}"

    class Meta:
        db_table_comment = "Historial de cambios de estado de las entradas."