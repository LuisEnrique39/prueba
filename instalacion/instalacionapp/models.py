from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.
class propiedades(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)    
    id_propiedad = models.CharField(max_length=250, null=True)
    tipo_propiedad = models.CharField(max_length=250, null=True)
    ubicacion = models.CharField(max_length=250, null=True, unique=False)
    metros_cuadrados = models.CharField(max_length=250, null=True,  unique=False)
    renta_o_venta = models.CharField(max_length=250, null=True)
    precio = models.CharField(max_length=300, null=True)
    n_habitaciones = models.CharField(max_length=250, null=True)
    estado_habitaciones = models.CharField(max_length=250, null=True)
    disponible = models.BooleanField(default=True,null=True) 
