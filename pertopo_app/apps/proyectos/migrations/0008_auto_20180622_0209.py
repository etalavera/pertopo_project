# Generated by Django 2.0.5 on 2018-06-22 02:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0007_auto_20180622_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_start_date',
            field=models.DateField(default=datetime.datetime.now, max_length=100),
        ),
    ]
