from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels={'email':'Email'}