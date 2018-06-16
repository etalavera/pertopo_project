from django.shortcuts import render_to_response
from apps.proyectos.models import *

# Create your views here.
def view_proyectos(request):
    template_name = "pertopo/proyectos/index.html"
    projects = Project.objects.all()
    return render_to_response(template_name, {'projects': projects})

def view_proyecto_id(request):
    template_name = "pertopo/proyectos/proyecto_id.html"
    return render_to_response(template_name, {})

def view_logout(request):
    template_name = "pertopo/close_session.html"
    return render(request, template_name)
