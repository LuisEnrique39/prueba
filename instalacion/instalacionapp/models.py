from importlib.resources import contents
from sqlite3 import Timestamp
from time import time, timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.


class Post(models.Model):
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


class Usuario(models.Model):
    nombre = models.CharField(max_length=250, null=True)
    apellidos = models.CharField(max_length=250, null=True)
    fecha = models.CharField(max_length=250, null=True)
    asunto = models.CharField(max_length=250, null=True)
    correo = models.CharField(max_length=250, null=True)
    comentarios = models.CharField(max_length=250, null=True)
    
    
class tienda(models.Model):
    user = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name='tienda', null=True) 
    nombre = models.CharField(max_length=250, null=True)
    apellido = models.CharField(max_length=250, null=True)
    correo = models.CharField(max_length=250, null=True, unique=False)
    numero = models.CharField(max_length=250, null=True, unique=False)
    pago = models.BooleanField(default=False,null=True)
    total = models.IntegerField()

class Dudas(models.Model):
    nombre = models.CharField(max_length=250, null=True)
    descripcion = models.CharField(max_length=250, null=True)

class Quejas(models.Model):
    nombre2 = models.CharField(max_length=250, null=True)
    descripcion2 = models.CharField(max_length=250, null=True)

class Contrata(models.Model):
    numero = models.FloatField(max_length=10, null=True)
    descripcion3 = models.CharField(max_length=250, null=True)
