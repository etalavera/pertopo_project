from django.http import JsonResponse
from django.core import serializers

from apps.proyectos.models import *
from apps.proyectos.forms import *


def save_add_task(request):
    if request.method == 'GET':
        return "running"

    if request.method == 'POST':
        form = LogbookForm(request.POST)
        if form.is_valid():
            project_id = request.POST['project']
            form.project = project_id
            form.log_date = request.POST['log_date']
            form.log_task = request.POST['log_task']
            form.log_meters = request.POST['log_meters']
            form.save(commit=True)
            response = {'status': 'true'}
            return JsonResponse(response)
        else:
            reponse = {'status': 'false'}
            return JsonResponse(response)
            print("error")
