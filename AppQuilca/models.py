from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


# Create your models here.
class Racquet(models.Model):
    raqueta = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    OPTIONS = (
        ("Used", "Usado"),
        ("New", "Nuevo"),
    )
    estado = models.CharField(max_length=10, choices=OPTIONS, null=True)
    fecha_creacion = models.DateTimeField(default=now(), blank=True)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="raquetas", null=True, blank=True)

    def __str__(self):
        return (f"Raqueta: {self.raqueta}, Precio: {self.precio} dólares, Fecha de creación: {self.fecha_creacion}, "
                f"Estado: {self.estado}")


class Comments(models.Model):
    raqueta = models.ForeignKey(to=Racquet, on_delete=models.CASCADE, related_name="comments")
    usuario = models.ForeignKey(to=User, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(default=now(), blank=True)


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
