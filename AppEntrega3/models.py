from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.CharField(max_length=50)

class Vendedores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.CharField(max_length=50)

class Productos(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    sku = models.IntegerField(default=1)

class Ventas(models.Model):
    numeroVenta = models.IntegerField()
    fecha = models.DateField()
    vendedor = models.CharField(max_length=40)
    cliente = models.CharField(max_length=40)

