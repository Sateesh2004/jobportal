from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Invalid username or password. Try again.',
    }
class SignUpForm(UserCreationForm):
 email = forms.EmailField(required=True, label='Email')
 class Meta:
  model = User
  fields = ['username','last_name', 'email','first_name']
  widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'USERNAME'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'FIRST NAME'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'LAST NAME'}),
            'email': forms.EmailInput(attrs={'placeholder': 'EMAIL'}),
        }
