import string
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)

    def __str__(self):
        return str(self.nombre)