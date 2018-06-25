from django.http import JsonResponse
from django.core import serializers

from apps.proyectos.models import *
from apps.proyectos.forms import *

def fillProjectsTable(resquest):
    projects        = Project.objects.all()
    response        = serializers.serialize('json', projects)
    return JsonResponse(response, safe=False)

def fillLogbookTable(request):
    response = {}
    print(request)
    if request.method == 'GET':
        logbook = Logbooks.objects.filter(project__id=1)
        response = serializers.serialize('json', logbook)
        return JsonResponse(response, safe=False)

    return JsonResponse(response, safe=False)
