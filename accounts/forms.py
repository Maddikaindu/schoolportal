from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import CustomUser

class CustomUserRegistrationForm(UserCreationForm):
    username=forms.CharField(max_length=100)
    email=forms.EmailField(required=True)
    password1=forms.CharField(max_length=100,widget=forms.PasswordInput)
    password2=forms.CharField(max_length=100,widget=forms.PasswordInput)
    class Meta:
        model=CustomUser
        fields=('username','email','password1','password2','role')

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput)
    password=forms.CharField(widget=forms.TextInput)
