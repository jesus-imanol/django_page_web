from django.db import models

class Agencia(models.Model):
    nombre_agencia = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_agencia
