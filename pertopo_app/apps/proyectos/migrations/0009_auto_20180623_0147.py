# Generated by Django 2.0.5 on 2018-06-23 01:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0008_auto_20180622_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_project',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_start_date',
            field=models.DateField(default=datetime.date.today, max_length=100),
        ),
    ]
