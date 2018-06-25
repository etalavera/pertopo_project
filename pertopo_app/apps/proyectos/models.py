from django.db import models
from datetime import date

# Create your models here.
class Person(models.Model):
    name        = models.CharField(blank=False, max_length=100)
    last_name   = models.CharField(blank=False, max_length=100)
    phone       = models.CharField(blank=False, max_length=100)
    email       = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return "%s %s" % (self.name, self.last_name)

class Custommer(models.Model):
    person  = models.ForeignKey(Person, on_delete=models.PROTECT,)
    address = models.CharField(blank=False, max_length=100)

class Project(models.Model):
    project_name                = models.CharField(blank=False, max_length=100)
    project_leader              = models.CharField(blank=False, max_length=100)
    project_address             = models.CharField(blank=False, max_length=100)
    project_city                = models.CharField(blank=False, max_length=100)
    project_seller              = models.CharField(blank=False, max_length=100)
    project_machine_operator    = models.CharField(blank=False, max_length=100)
    project_machine             = models.CharField(blank=False, max_length=100)
    project_custommer           = models.CharField(blank=False, max_length=100)
    project_start_date          = models.DateField(blank=False, max_length=100, default=date.today)
    project_end_date            = models.CharField(blank=True, max_length=100)
    project_estimate_meters     = models.CharField(blank=False, max_length=100)
    project_real_meters         = models.CharField(blank=True, max_length=100)
    project_price_per_meter     = models.CharField(blank=False, max_length=100)
    project_observations        = models.TextField(blank=True)
    project_progress            = models.CharField(blank=False, max_length=100, default='0')

    def __str__(self):
        return "%s" % (self.project_name)

class Logbooks(models.Model):
    project             = models.ForeignKey(Project, on_delete=models.PROTECT)
    log_date            = models.CharField(blank=False, default=date.today, max_length=100)
    log_task            = models.CharField(blank=False, default='NULL', max_length=100)
    log_meters          = models.CharField(blank=False, default='0', max_length=100)
    log_total_meters    = models.CharField(blank=False, default='0', max_length=100)
