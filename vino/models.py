from django.db import models
from bases.models import ClaseModelo
class Unidad(models.Model):
    medida=models.CharField(max_length=10)
    def __str__(self):
         return self.medida
class Bodega(models.Model):
    nombre=models.CharField(max_length=30)
    numero=models.CharField(max_length=30, blank=True ,null=True)
    email=models.CharField(max_length=30 ,blank=True ,null=True)
    def __str__(self):
        return self.nombre
class Reserva(models.Model):
    tipo=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=50, blank=True ,null=True)
    def __str__(self):
        return self.tipo

class Cepa(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100 , blank=True ,null=True)
    estado=models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
# Create your models here.
class Vino(models.Model):
    nombre=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=100 , blank=True ,null=True)
    codigo=models.CharField(max_length=30 ,unique=True)
    precioventa=models.FloatField()
    foto=models.ImageField(blank=True, null=True)
    reserva=models.ForeignKey(Reserva , on_delete=models.CASCADE)
    bodega=models.ForeignKey(Bodega , on_delete=models.CASCADE)
    cepa=models.ForeignKey(Cepa, on_delete=models.CASCADE)
    unidad=models.ForeignKey(Unidad, on_delete=models.CASCADE)
    existencia=models.IntegerField(default=0)
    ultimacompra=models.DateField(blank=True , null=True)
    sm=models.IntegerField(blank=True , null=True)
    

    def __str__(self):
            return '{}'.format(self.nombre)
class Meta:
        verbose_name_plural = "Productos"
        
