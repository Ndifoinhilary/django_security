from django import forms 
from authentication import models 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    captcha = ReCaptchaField()
    class Meta:
        model = User 
        
        fields = ['email', 'username','captcha']




