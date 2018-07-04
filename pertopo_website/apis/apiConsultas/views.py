from django.http import JsonResponse
from django.core import serializers

from apps.website.models import *

def consultaVacantes(request):

    if request.method == 'GET':
