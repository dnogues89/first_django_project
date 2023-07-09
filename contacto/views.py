from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def landing(requests):
    contact_form = ContactForm()
    
    context = {"my_form":contact_form}
    return render(requests,'contacto/landing.html',context)