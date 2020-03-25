# Generated by Django 3.0.3 on 2020-03-25 12:26

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20200221_1843'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['id'], 'verbose_name': 'Restaurante', 'verbose_name_plural': 'Restaurantes'},
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre del restaurante'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='pnt',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Punto de ubicación'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='twenty_four_hours',
            field=models.BooleanField(default=False, verbose_name='¿Está abierto 24 horas?'),
        ),
    ]