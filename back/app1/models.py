from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
# Objetos a definir:

GENERO = [
    ('f','femenino'),
    ('m','masculino'),
]

Region = [
    ('I','TARAPACA),
    ('II','ANTOFAGASTA'),
    ('III','ATACAMA'),
    ('IV','COQUIMBO'),
    ('V','VALPARAISO'),
    ('VI','RANCAGUA'),
    ('VII','MAULE'),
    ('VIII','BIO BIO'),
    ('IX','ARAUCANIA'),
    ('X','LOS LAGOS'),
    ('XI','AYSEN'),
    ('XII','MAGALLANES'),
    ('XIII','METROPOLITANA'),
    ('XIV','LOS RIOS'),
    ('XV','ARICA Y PARINACOTA'),
    ('XVI','NUBLE'),

]


class Pasajero(models.Model):
    rut = models.ForeignKey()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)


class Comprador(models.Model):
    c_ide = models.AutoField(primary_key=True)
    n_boleta = models.IntegerField()
    c_nombre = models.CharField(max_length=30)
    c_apellido = models.CharField(max_length=30)
    c_telefono = models.IntegerField()
    c_email = models.EmailField(max_length=50)

class Boleta(models.Model):
    n_boleta = models.AutoField(primary_key=True)
    id_avioneta = models.IntegerField()
    rut_chofer = models.CharField(max_length=15)
    origen = models.CharField(max_length=50, choices=Region, blank=True, default='')
    destino = models.CharField(max_length=50, choices=Region, blank=True, default='')
    hrsalida = models.DateTimeField()
    hrllegada = models.DateTimeField()
    costo = models.IntegerField()


class Avion(models.Model):
    id_avioneta = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    acientos = models.IntegerField()


    

