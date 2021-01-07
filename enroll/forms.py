from django import forms
from django.core import validators
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name', 'email', 'password']
        labels={'name':'Enter Name', 'email':'Enter Email', 'password':'Enter Password'}
        error_messages={
            'name':{'required': 'Please Enter Your Name'},
            'email':{'required': 'Please Enter Your Valid EmailAdress'},
            'password':{'required': 'Please Enter  Password'}
        }
        widgets={
            'password':forms.PasswordInput,
            'name':forms.TextInput(attrs={'class':'myclass', 'placeholder':'Yaha nam Likhiye'})
        }