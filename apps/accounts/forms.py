from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form_control',
            'placeholder': 'Password'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form_control',
            'placeholder': ' Confirm Password'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form_control',
            'placeholder': 'Username'
        }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form_control',
            'placeholder': 'Email'
        }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form_control',
            'placeholder': 'Username'
        }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form_control',
            'placeholder': 'Email'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form_control',
            'placeholder': 'Password'
        }
    ))

