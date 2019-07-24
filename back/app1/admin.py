from __future__ import unicode_literals
from django.contrib import admin
from .models import Pasajero , Comprador, Boleta, Avion



# Register your models here.
admin.site.Register(Pasajero)
admin.site.Register(Comprador)
admin.site.Register(Boleta)
admin.site.Register(Avion)
