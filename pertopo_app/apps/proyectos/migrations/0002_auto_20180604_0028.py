# Generated by Django 2.0.5 on 2018-06-04 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
