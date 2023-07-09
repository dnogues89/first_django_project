from django.urls import path
from WhatApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='Home'),
    path('prueba/',views.prueba,name='Prueba'),
]

urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)