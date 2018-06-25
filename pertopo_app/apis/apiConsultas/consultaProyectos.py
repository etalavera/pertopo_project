from django.http import JsonResponse
from django.core import serializers

from apps.proyectos.models import *
from apps.proyectos.forms import *

def query_projects(request):
    if request.method == 'GET':
        response = Project.objects.all()
        response = serializers.serialize('json', response)
        return JsonResponse(response, safe=False)
    if request.method == 'POST':
        pass

def query_logbook(request):
    if request.method == 'GET':
        response = Logbooks.objects.filter(project__id=request.GET['project_id'])
        response = serializers.serialize('json', response)
        return JsonResponse(response, safe=False)

    if request.method == 'POST':
        pass
