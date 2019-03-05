from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from .models import Profile, CustomUser
from django.core.mail import send_mail
from django.conf import settings

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model  = CustomUser
        fields = ["username", "email", 'phone', 'first_name', 'last_name', "password1", "password2"]
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Dirección de correo ya en uso.')
        return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        
        send_mail(
            f'Nuevo usuario creado: {user.username}',
            'Comprueba los datos y activa la cuenta si procede.',
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_ADMIN],
            fail_silently=False,
        )

        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model  = CustomUser
        fields = ["email", 'first_name', 'last_name',]    

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model  = Profile
        fields = ['image']