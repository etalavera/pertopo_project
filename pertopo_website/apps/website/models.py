from django.db import models

# Create your models here.
class Vacantes(models.Model):
    nombre = models.CharField(blank=False, max_length=100)
    zona = models.CharField(blank=False, max_length=100)
    requisitos = models.CharField(blank=False, max_length=100)
    oferta = models.CharField(blank=False, max_length=100)
    mensaje = models.TextField(blank=True)

class Candidato(models.Model):
    vacante = models.ManyToManyField(Vacantes)
    nombre = models.CharField(blank=True, max_length=100)
    apellidos = models.CharField(blank=True, max_length=100)
    telefono = models.CharField(blank=True, max_length=100)
    cv = models.FileField(upload_to='static/cvs')
