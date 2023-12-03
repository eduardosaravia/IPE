from django.db import models
from PIL import Image

class Producto(models.Model):
    producto = models.CharField(max_length=100, default='PEPELMA')
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.CharField(max_length=10, default='M2')
    precio_distribuidor = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    caja = models.PositiveIntegerField(default=1)
    presentacion = models.CharField(max_length=100, default='CAJAS x 2 M2')
    moneda = models.CharField(max_length=10, choices=[('USD', 'Dólar estadounidense'), ('SOL', 'Sol peruano')], default='USD')
    imagen = models.ImageField(upload_to='productos', default='images/default.jpg')
    imagen_instalada = models.ImageField(upload_to='productos', default='images/default.jpg')
    categoria = models.CharField(max_length=100, default='SIN CATEGORIA')
    en_oferta = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.imagen.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.imagen.path)
