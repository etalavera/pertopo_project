from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    template_name = 'overerts/index.html'
    return render(request, template_name, {})

def bolsa(request):
    template_name = 'overerts/bolsa.html'
    vacantes = Vacantes.objects.all()
    return render(request, template_name, {'vacantes': vacantes})
