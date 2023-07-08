from django.db import models

# Create your models here.

class Servicio(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=700)
    image=models.ImageField(upload_to='ServiciosBot')
    try_it_numb=models.IntegerField()
    updated=models.DateTimeField(auto_now_add=True)
    created=models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
        
    def __str__(self) -> str:
        return self.title
    