from django.db import models
from django.contrib.auth.models import AbstractUser


class MiUsuario(AbstractUser):
    telefono = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    fecha_nacimiento = models.DateField(
        blank=True,
        null=True
    )

    biografia = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table_comment = "Usuarios registrados en el diario personal."

# Create your models here.
