from django import forms
from .models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'name':TextInput(attrs={'placeholder':"Your Name",'name':"name"}),
            'phone':TextInput(attrs={'placeholder':"Your Phone",'name':"phone"}),
            'email':TextInput(attrs={'placeholder':"Your E-mail",'name':"email"}),
            'subject':TextInput(attrs={'placeholder':"Subject",'name':"subject"}),
            'message':Textarea(attrs={'placeholder':"Message",'name':"message",'rows':"4"}),
         }