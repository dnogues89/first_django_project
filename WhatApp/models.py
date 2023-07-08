from django.db import models

# Create your models here.

class WhatsappMsg(models.Model):
    tipo = models.CharField(max_length=30)
    wap_id = models.CharField(max_length=70)
    telefono = models.CharField(max_length=15)
    mime_type = models.CharField(max_length=70)
    sha256 = models.CharField(max_length=70)
    media_id = models.CharField(max_length=30)


class Cliente(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    email = models.EmailField(verbose_name='Mail')
    telefono = models.CharField(max_length=15, verbose_name='Telefono')
    estatus = models.IntegerField()

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} Telefono: {self.telefono} Estatus: {self.estatus}'
    
class Error(models.Model):
    error = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return f'Proyecto: {self.num_proyecto} Inicio: {self.inicio} Estatus: {self.finalizado}'
    