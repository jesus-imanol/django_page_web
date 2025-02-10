from django.db import models
from .Modelo import Modelo
from .Agencia import Agencia
class ModeloAgencia(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)
    agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.modelo} - {self.agencia}"
