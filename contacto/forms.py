from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name',required=True)
    email = forms.EmailField(label='E-mail',required=True)
    message = forms.CharField(label='Message',widget=forms.Textarea)