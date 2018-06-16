from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    phone = models.CharField(blank=False, max_length=100)
    email = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return "%s %s" % (self.name, self.last_name)

class Custommer(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE,)
    address = models.CharField(blank=False, max_length=100)

class Project(models.Model):
    project_name = models.CharField(blank=False, max_length=100)
    project_leader = models.CharField(blank=False, max_length=100)
    progress = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return "%s" % (self.project_name)
