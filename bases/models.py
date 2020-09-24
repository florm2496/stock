from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey
# Create your models here.
class ClaseModelo(models.Model):
    estado=models.BooleanField(default=True)
    fc =models.DateTimeField(auto_now_add=True)#esto tomara valor solo cuando cree el objeto 
    fm=models.DateTimeField(auto_now=True)#cada vez que haya una transaccion
    uc=models.ForeignKey(User , on_delete=models.CASCADE) #usuario creador
    un=models.IntegerField(blank=True , null=True)

    class Meta:
        abstract=True
    

