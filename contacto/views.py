from django.shortcuts import render,redirect
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def landing(requests):
    contact_form = ContactForm()
    if requests.method == 'POST':
        contact_form=ContactForm(data=requests.POST)
        if contact_form.is_valid():
            nombre=requests.POST.get('name')
            email=requests.POST.get('email')
            message=requests.POST.get('message')
            # try:
            send_mail = EmailMessage('New message from web',f'New message from: {nombre}\nE-Mail: {email}\nSends: {message}','',['dnogues@espasa.com.ar'],reply_to=[email])
            send_mail.send()
            return redirect("/contacto/?valid")
            # except:
            #     return redirect('/contacto/?not_valid')
            
    context = {"my_form":contact_form}
    return render(requests,'contacto/landing.html',context)