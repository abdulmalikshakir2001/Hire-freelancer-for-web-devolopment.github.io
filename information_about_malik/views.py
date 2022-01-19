from django.shortcuts import redirect, render
from information_about_malik.forms import Contact_Malik_Form
from.forms import Contact_Malik_Form

from information_about_malik.models import Contact_Malik

# Create your views here.
def home(request):
    if request.method=="POST":
        data=Contact_Malik_Form(request.POST)
        if data.is_valid():
            # Malik_Form_with_data.save()
            name=data.cleaned_data['name']
            email=data.cleaned_data['email']
            subject=data.cleaned_data['subject']
            message=data.cleaned_data['message']
            client=Contact_Malik(name=name,email=email,subject=subject,message=message)
            client.save()
            return redirect('/')
    else:
        data=Contact_Malik_Form(label_suffix=" *")
    return render(request,'home.html',{'C_M_Form':data})
def about(request):
    return render(request,'about.html')
