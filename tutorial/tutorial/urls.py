"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tutorial.view import HomePageView,AddAgenciaView,AddLogroView,delete_modelo,GenericView,ElementsView,AddModelView,AboutPageView,BasePageView,CarrerasCreateView, IndexView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name= 'index'),
    path('about', AboutPageView.as_view(), name= 'about'),
    path('generic', GenericView.as_view(), name= 'generic'),
    path('elements', ElementsView.as_view(), name= 'elements'),
    path('elements/edit_modelo/<int:modelo_id>/', ElementsView.as_view(), name='edit_modelo'),
    path('elements/delete_modelo/<int:modelo_id>/', delete_modelo, name='delete_modelo'),
    path('carrera/crear',CarrerasCreateView.as_view(), name= 'carrera_crear'),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'logout.html'), name= 'logout'),
    path('addmodel/', AddModelView.as_view(), name='addmodel'),
    path('addlogro', AddLogroView.as_view(template_name = 'addlogro.html'), name='addlogro'),
    path('addagencia', AddAgenciaView.as_view(template_name = 'addagencia.html'), name='addagencia'),

]
