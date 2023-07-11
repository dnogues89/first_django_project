from django.db import models

# Create your models here.
class Categorie(models.Model):
    cat_name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'
    
    def __str__(self) -> str:
        return self.cat_name
        
class Product(models.Model):
    code = models.CharField(max_length=10,primary_key=True)
    brand = models.CharField(max_length=10)
    family = models.CharField(max_length=10)
    model = models.CharField(max_length=70)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def __str__(self) -> str:
        return f'{self.code} / {self.model}'
    
class Pub(models.Model):
    code = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store',null=True,blank=True)
    price = models.IntegerField()
    color = models.CharField(max_length=20)
    available = models.BooleanField(verbose_name='Ava')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'publication'
        verbose_name_plural = 'publications'
        
    def __str__(self) -> str:
        return f'{self.code} / {self.color}'