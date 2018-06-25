from django.urls import path
from . import saveForms

urlpatterns = [
    path('save_add_task', saveForms.save_add_task, name='save_add_task'),
]
