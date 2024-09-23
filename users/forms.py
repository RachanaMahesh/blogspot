from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #by default required = True jence haven't addes

    class Meta: # gives us nested namespace for configuration and kepps the configuration in one space
        model = User # becoz whenever data is validated its going to create user so model = User
        fields = ['username', 'email', 'password1', 'password2']