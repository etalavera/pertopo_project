from django.urls import path
from . views

urlpatterns = [
    path('consultaVacantes', views.consultaVacantes, name='consultaVacantes'),
]
