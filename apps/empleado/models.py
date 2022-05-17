import string
from django.db import models

from apps.equipo.models import Equipo


# Create your models here.


class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    equipo = models.ManyToManyField(Equipo, through='Mantenimiento')

    def __str__(self):
        return str(self.nombre)

class Mantenimiento(models.Model):
    EmpleadoId = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    EquipoId = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=30)
    tipoMantenimiento = models.CharField(max_length=30)

    def __str__(self):
        return str(self.fecha)