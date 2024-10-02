from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(
        max_length=200, verbose_name="nombre"
    )  # verbose_name es para cambiar el nombre en el admin de django
    description = models.TextField(max_length=300, verbose_name="descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    available = models.BooleanField(default=True, verbose_name="disponible")
    photo = models.ImageField(
        upload_to="logos", null=True, blank=True, verbose_name="foto"
    )  # upload_to='products' es para guardar las imagenes en la carpeta products
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="fecha de creación"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="fecha de actualización"
    )

    def __str__(self):
        return self.name
