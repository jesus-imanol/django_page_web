from django.db import models
from .Modelo import Modelo

class Logro(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return self.titulo
