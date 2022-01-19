from django import forms
from django.forms import fields, widgets
from.models import Contact_Malik

class Contact_Malik_Form(forms.ModelForm):
    class Meta:
        model=Contact_Malik
        fields=['name','email','subject','message']
        widgets={
            'name':forms.TextInput(attrs={'class':'form_Name s_Form'}),
            'email':forms.EmailInput(attrs={'class':'form_Email s_Form'}),
            'subject':forms.TextInput(attrs={'class':'form_Subject s_Form s_Form1'}),
            'message':forms.TextInput(attrs={'class':'form_Message s_Form'})
        }