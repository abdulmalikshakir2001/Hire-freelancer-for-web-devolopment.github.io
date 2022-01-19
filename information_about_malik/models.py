from django.db import models

# Create your models here.
class Contact_Malik(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=200)
