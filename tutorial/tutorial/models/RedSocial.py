from django.db import models
from .Modelo import Modelo

class RedSocial(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)
    tipo = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return f"{self.tipo} - {self.url}"
