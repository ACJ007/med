from django.db import models

 

# Create your models here.

class posts(models.Model):

    title=models.CharField(max_length=20)

    content=models.CharField(max_length=40)

    

class feedbacks(models.Model):

    heading=models.CharField(max_length=20)

    content=models.CharField(max_length=40)

 



from django import forms

from django.contrib.auth.models import User

from .import models

 

 

class RegisterForm(forms.ModelForm):

    class Meta:

        model=User

        fields=['username','email','password','first_name','last_name',]

        widgets={

            'password':forms.PasswordInput(),

            'email':forms.EmailInput()

            

        }