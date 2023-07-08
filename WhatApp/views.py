from django.shortcuts import render , HttpResponse


# Create your views here.

def home(requests):
    return render(requests,'WhatApp/index.html')


def landing(requests):
    return render(requests,'WhatApp/landing.html')

def prueba (requests):
    return render(requests,'WhatApp/prueba.html')

