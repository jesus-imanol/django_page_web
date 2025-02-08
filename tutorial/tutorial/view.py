from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Carrera
from django.shortcuts import redirect
from .views import CarreraForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index(request):
    return HttpResponse("Hello, World!")

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
        context = {'form': form}
        return self.render_to_response(context)
    def post(self, request, *args, **kwargs):
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
        context = {'form': form}
        return self.render_to_response(context)    
