# Generated by Django 2.0.5 on 2018-06-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0010_auto_20180623_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_observations',
            field=models.TextField(blank=True),
        ),
    ]
