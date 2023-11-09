from django import forms
from .models import Seekers

class SeekerForm(forms.ModelForm):
    class Meta:
        model = Seekers
        fields = ['user_name','phone_number' ,'email', 'resume', 'education', 'work_experience', 'skills', 'portfolio',  'linkedin_profile', 'github_profile', 'additional_information']
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'resume': forms.FileInput(attrs={'placeholder': 'Enter your email'}),
            'education': forms.Textarea(attrs={'placeholder': 'Enter your educational background'}),
            'work_experience': forms.Textarea(attrs={'placeholder': 'Enter your work experience'}),
            'skills': forms.Textarea(attrs={'placeholder': 'Enter your skills'}),
            'portfolio': forms.URLInput(attrs={'placeholder': 'Enter your portfolio URL'}),
            'linkedin_profile': forms.URLInput(attrs={'placeholder': 'Enter your LinkedIn profile URL'}),
            'github_profile': forms.URLInput(attrs={'placeholder': 'Enter your GitHub profile URL'}),
            'additional_information': forms.Textarea(attrs={'placeholder': 'Enter any additional information'}),
        }
