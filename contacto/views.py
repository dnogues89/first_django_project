from django.shortcuts import render,redirect
from .forms import ContactForm

# Create your views here.
def landing(requests):
    contact_form = ContactForm()
    if requests.method == 'POST':
        contact_form=ContactForm(data=requests.POST)
        if contact_form.is_valid():
            nombre=requests.POST.get('name')
            email=requests.POST.get('email')
            message=requests.POST.get('message')
            return redirect("/contacto/?valid")
    context = {"my_form":contact_form}
    return render(requests,'contacto/landing.html',context)