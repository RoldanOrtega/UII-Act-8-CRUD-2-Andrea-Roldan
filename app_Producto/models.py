from django.db import models

# Create your models here.

class Producto(models.Model): # Cambiado de Comic a Producto
    TIPO_PRODUCTO_CHOICES = [
        ('fisico', 'Físico'),
        ('digital', 'Digital'),
    ]

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=17, unique=True, help_text="Formato: XXX-X-XXX-XXXXX-X")
    tipo_producto = models.CharField(max_length=10, choices=TIPO_PRODUCTO_CHOICES, default='fisico')

    def __str__(self):
        return f'{self.titulo} por {self.autor}' # Mantiene la descripción de cómic, pero es un Producto