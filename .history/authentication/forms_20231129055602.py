from django import forms 
from authentication import models 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsercreationForm


class RegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=6, widget = forms.PasswordInput)
    password1 = forms.CharField(min_length=6, widget = forms.PasswordInput)
    
    class Meta:
        model = User 
        
        fields = ['emial', 'username', 'password','password1']