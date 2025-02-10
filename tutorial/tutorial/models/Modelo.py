from django.db import models
from django.utils.timezone import now

class Modelo(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(default=now)
    pais = models.CharField(max_length=50)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    nacionalidad = models.CharField(max_length=100) 
    edad = models.IntegerField(default=0) 

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
