from django import forms 
from authentication import models 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        
        fields = ['emial', 'username', 'password','password2']