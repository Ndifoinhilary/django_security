from django import forms 
from authentication import models 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User 
        
        fields = ['email', 'username', 'password',]