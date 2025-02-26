from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Carrera, Modelo,Agencia,Logro,ModeloAgencia
from django.shortcuts import redirect
from .views import CarreraForm
from .views import ModeloAgenciaForm, AgenciaForm, ModeloForm, LogroForm
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden



class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Carrera
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["saludo"] = "Hola de nuevo"
        context["lista"] = Carrera.objects.all()    
        return context

    @method_decorator(login_required, name='dispatch')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
class BasePageView(TemplateView):
    template_name = 'base.html'

class CarrerasCreateView(TemplateView):
    template_name = 'carreras_form.html'
    def get(self, request, *args, **kwargs):
        form = CarreraForm()
        context = {'form': form,'has_perm': request.user.has_perm('add_carrera')}
        return self.render_to_response(context)
    def post(self, request, *args, **kwargs):
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
        context = {'form': form, 'has_perm': request.user.has_perm('add_carrera')}
        return self.render_to_response(context)
    
class IndexView(TemplateView):
    template_name = 'index.html'
@login_required
def delete_modelo(request, modelo_id):
    # Get the model instance by its ID
    modelo = get_object_or_404(Modelo, id=modelo_id)
    
    # Check if the user is authorized to delete the model
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to delete this model.")
    
    # Delete the model instance
    modelo.delete()
    
    # Redirect to the elements page after deletion
    return redirect('elements')

class ElementsView(TemplateView):


    template_name = 'elements.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener todos los modelos, agencias y logros para mostrarlos en el formulario
        context['modelos'] = Modelo.objects.all()
        context['agencias'] = Agencia.objects.all()
        context['logros'] = Logro.objects.all()
        context['modelo_agencia'] = ModeloAgencia.objects.all()

        # Crear instancias de los formularios vacíos
        context['modelo_form'] = ModeloForm()
        context['agencia_form'] = AgenciaForm()
        context['modelo_agencia_form'] = ModeloAgenciaForm()
        context['logro_form'] = LogroForm()

        # Verificar si se está editando un modelo específico
        modelo_id = self.kwargs.get('modelo_id')
        if modelo_id:
            modelo = get_object_or_404(Modelo, id=modelo_id)
            context['modelo_form'] = ModeloForm(instance=modelo)  # Pre-cargar el modelo en el formulario

        return context
    
    def post(self, request, *args, **kwargs):
        modelo_id = request.POST.get('modelo_id')
        # Si el modelo_id existe, obtenemos el modelo para actualizarlo
        if modelo_id:
            modelo = get_object_or_404(Modelo, id=modelo_id)
            modelo_form = ModeloForm(request.POST, instance=modelo)  # Usar 'instance' para editar el modelo
        else:
            modelo_form = ModeloForm(request.POST)  # Si no se pasa un modelo_id, creamos uno nuevo

        agencia_form = AgenciaForm(request.POST)
        modelo_agencia_form = ModeloAgenciaForm(request.POST)
        logro_form = LogroForm(request.POST)

        # Validar y guardar el formulario del modelo
        if modelo_form.is_valid():
            modelo_form.save()  # Actualizar el modelo existente o crear uno nuevo si no tiene modelo_id

        if agencia_form.is_valid():
            agencia_form.save()  # Guardar la agencia si el formulario es válido

        if modelo_agencia_form.is_valid():
            modelo_agencia_form.save()  # Guardar la relación modelo-agencia

        if logro_form.is_valid():
            logro_form.save()  # Guardar el logro si el formulario es válido

        # Redirigir a la misma página después de guardar
        return redirect('elements')
class GenericView(TemplateView):
    template_name = 'generic.html'

from django.shortcuts import render
@method_decorator(permission_required('tutorial.addmodel', login_url='/login', raise_exception=False), name='dispatch')
class AddModelView(TemplateView):
    template_name = 'addmodel.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modelo_form'] = ModeloForm()
        context['agencia_form'] = AgenciaForm()
        context['modelo_agencia_form'] = ModeloAgenciaForm()
        context['logro_form'] = LogroForm()
        return context

    def post(self, request, *args, **kwargs):
        modelo_form = ModeloForm(request.POST)
        agencia_form = AgenciaForm(request.POST)
        modelo_agencia_form = ModeloAgenciaForm(request.POST)
        logro_form = LogroForm(request.POST)

        if modelo_form.is_valid():
            modelo_form.save()
            return redirect('elements') # Redirigir a una página de tu elección después de guardar

        if agencia_form.is_valid():
            agencia_form.save()
            return redirect('elements')

        if modelo_agencia_form.is_valid():
            modelo_agencia_form.save()
            return redirect('elements')

        if logro_form.is_valid():
            logro_form.save()
            return redirect('elements')

        context = {
            'modelo_form': modelo_form,
            'agencia_form': agencia_form,
            'modelo_agencia_form': modelo_agencia_form,
            'logro_form': logro_form
        }
        return self.render_to_response(context)
    
from django.shortcuts import render
class AddLogroView(TemplateView):
    template_name = 'addlogro.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modelo_form'] = ModeloForm()
        context['agencia_form'] = AgenciaForm()
        context['modelo_agencia_form'] = ModeloAgenciaForm()
        context['logro_form'] = LogroForm()
        return context

    def post(self, request, *args, **kwargs):
        modelo_form = ModeloForm(request.POST)
        agencia_form = AgenciaForm(request.POST)
        modelo_agencia_form = ModeloAgenciaForm(request.POST)
        logro_form = LogroForm(request.POST)

        if modelo_form.is_valid():
            modelo_form.save()
            return redirect('elements') # Redirigir a una página de tu elección después de guardar

        if agencia_form.is_valid():
            agencia_form.save()
            return redirect('elements')

        if modelo_agencia_form.is_valid():
            modelo_agencia_form.save()
            return redirect('elements')

        if logro_form.is_valid():
            logro_form.save()
            return redirect('elements')

        context = {
            'modelo_form': modelo_form,
            'agencia_form': agencia_form,
            'modelo_agencia_form': modelo_agencia_form,
            'logro_form': logro_form
        }
        return self.render_to_response(context)

class AddAgenciaView(TemplateView):
    template_name = 'addagencia.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modelo_form'] = ModeloForm()
        context['agencia_form'] = AgenciaForm()
        context['modelo_agencia_form'] = ModeloAgenciaForm()
        context['logro_form'] = LogroForm()
        return context

    def post(self, request, *args, **kwargs):
        modelo_form = ModeloForm(request.POST)
        agencia_form = AgenciaForm(request.POST)
        modelo_agencia_form = ModeloAgenciaForm(request.POST)
        logro_form = LogroForm(request.POST)

        if modelo_form.is_valid():
            modelo_form.save()
            return redirect('elements')

        if agencia_form.is_valid():
            agencia_form.save()
            return redirect('elements')

        if modelo_agencia_form.is_valid():
            modelo_agencia_form.save()
            return redirect('elements')

        if logro_form.is_valid():
            logro_form.save()
            return redirect('elements')

        context = {
            'modelo_form': modelo_form,
            'agencia_form': agencia_form,
            'modelo_agencia_form': modelo_agencia_form,
            'logro_form': logro_form
        }
        return self.render_to_response(context)