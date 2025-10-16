from django.contrib import admin

# Register your models here.

from .models import Producto # Cambiado de Comic a Producto

admin.site.register(Producto) 