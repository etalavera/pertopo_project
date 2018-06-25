from django.urls import path
from . import consultaProyectos

urlpatterns = [
    path('query_projects', consultaProyectos.query_projects, name='fill_project_table'),
    path('query_logbook', consultaProyectos.query_logbook, name='fill_logbook_table'),
]
