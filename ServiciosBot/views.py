from django.shortcuts import render
from ServiciosBot.models import Servicio

# Create your views here.
def services(requests):
    
    services = Servicio.objects.all()
  
    return render(requests,'ServiciosBot/services.html',{'services':services})