from django import forms
from ..models import Modelo, Agencia, ModeloAgencia, Logro


class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'pais', 'altura', 'peso', 'descripcion', 'nacionalidad', 'edad'] 

class AgenciaForm(forms.ModelForm):
    class Meta:
        model = Agencia
        fields = ['nombre_agencia', 'pais', 'ciudad']

class ModeloAgenciaForm(forms.ModelForm):
    class Meta:
        model = ModeloAgencia
        fields = ['modelo', 'agencia']

class LogroForm(forms.ModelForm):
    class Meta:
        model = Logro
        fields = ['modelo', 'titulo', 'descripcion', 'fecha']  