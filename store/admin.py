from django.contrib import admin
from .models import Categorie, Product, Pub

# Register your models here.
class PubAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('code','color','price','available',)
    

admin.site.register(Categorie)
admin.site.register(Product)
admin.site.register(Pub,PubAdmin)    