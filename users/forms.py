from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from .models import Profile, CustomUser

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model  = CustomUser
        fields = ["username", "email", 'phone', 'first_name', 'last_name', "password1", "password2"]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model  = CustomUser
        fields = ["username", "email", 'phone', 'first_name', 'last_name',]    

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model  = Profile
        fields = ['image']