from django.shortcuts import render_to_response, render

from apps.proyectos.models import *
from apps.proyectos.forms import *

# Create your views here.
def view_proyectos(request):
    template_name   = "pertopo/proyectos/index.html"
    form = LogbookForm()
    return render(request, template_name, {'form': form})

def view_proyecto_id(request, project_id):
    template_name   = "pertopo/proyectos/proyecto_id.html"
    by_id           = Project.objects.get(pk=project_id)
    context         = {'proyecto': by_id}
    return render_to_response(template_name, context)

def view_flash_message(request):
    return render(request, template_name)

def view_proyectos_add(request):
    template_name   = "pertopo/proyectos/add_project.html"

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return view_proyectos(request)
        else:
            #return view_flash_message(request)
            print(form.errors)
    else:
        form = ProjectForm()

    context = {'form': form}

    return render(request, template_name, context)

def view_logout(request):
    template_name   = "pertopo/close_session.html"
    return render(request, template_name)
