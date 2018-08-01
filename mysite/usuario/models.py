from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    imagen = models.CharField(max_length=100)

class Servicios(models.Model):
    usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    nombre_serv = models.CharField(max_length=100)

class Fila(models.Model):
    nombre = models.CharField(max_length=150)
    agencia = models.CharField(max_length=100)
    provincia = models.CharField(max_length=150)
    fecha = models.CharField(max_length=150)
    total = models.IntegerField()