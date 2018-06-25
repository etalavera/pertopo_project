from django.urls import path
from . import views
from . import api_tables

urlpatterns = [
    path('', views.view_proyectos, name='index'),
    path('<int:project_id>/', views.view_proyecto_id, name='proyecto_id'),
    path('add', views.view_proyectos_add, name='add_project'),
]
