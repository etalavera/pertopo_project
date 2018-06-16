# Generated by Django 2.0.5 on 2018-06-10 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_auto_20180604_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custommer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Poject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_leader', models.CharField(max_length=100)),
            ],
        ),
    ]