from django.shortcuts import render , redirect
from contacto.forms import ContactForm

# Create your views here.

def home(requests):
    #This includes contact form at the index
    contact_form = ContactForm()
    if requests.method == 'POST':
        contact_form=ContactForm(data=requests.POST)
        if contact_form.is_valid():
            nombre=requests.POST.get('name')
            email=requests.POST.get('email')
            message=requests.POST.get('message')
            return redirect("/?valid")
    context = {"my_form":contact_form}
    return render(requests,'WhatApp/index.html',context)

def prueba (requests):
    return render(requests,'WhatApp/prueba.html')

