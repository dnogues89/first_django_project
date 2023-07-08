from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    name=models.CharField(max_length=50)
    updated=models.DateTimeField(auto_now_add=True)
    created=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        
    def __str__(self) -> str:
        return self.name
    
class Post(models.Model):
    title=models.CharField(max_length=300)
    content=models.CharField(max_length=20000)
    image=models.ImageField(upload_to='blog',null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    updated=models.DateTimeField(auto_now_add=True)
    created=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
        
    def __str__(self) -> str:
        return self.title
    
