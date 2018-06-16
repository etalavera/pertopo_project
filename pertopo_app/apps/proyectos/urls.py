from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_proyectos, name='index'),
    path('<int:project_id>)/', views.view_proyecto_id, name='proyecto_id'),
]
