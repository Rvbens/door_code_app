from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from .models import Profile, UserCreation

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model  = UserCreation
        fields = ["username", "email", 'first_name', 'last_name', 'phone', "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model  = User
        fields = ["username", "email"]    

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model  = Profile
        fields = ['image']