from django import forms
from .models import Job
JOB_CATEGORIES = [
    ('Select the Category', 'Select the Category'),
    ('Marketing', 'Marketing'),
    ('Customer Service', 'Customer Service'),
    ('Human Resource', 'Human Resource'),
    ('Project Management', 'Project Management'),
    ('Business Development', 'Business Development'),
    ('Sales & Communication', 'Sales & Communication'),
    ('Teaching & Education', 'Teaching & Education'),
    ('Design & Creative', 'Design & Creative'),
]
class Jobform(forms.ModelForm):
     jobtitle = forms.ChoiceField(choices=JOB_CATEGORIES, label='Job Category')
     class Meta:
        model = Job
        fields = ['jobtitle', 'joblocation', 'companyname', 'jobtype', 'industry', 'skills', 'description', 'qualification', 'experience', 'salary', 'url', 'email', 'linkedin']
        labels = {
            'jobtitle': 'Job Title',
            'joblocation': 'Job Location',
            'companyname': 'Company Name',
            'jobtype': 'Job Type',
            'industry': 'Industry',
            'skills': 'Skills',
            'description': 'Description',
            'qualification': 'Qualification',
            'experience': 'Experience',
            'salary': 'Salary',
            'url': 'URL',
            'email': 'Email',
            'linkedin': 'LinkedIn',
        }
        widgets = {
            'jobtitle': forms.TextInput(attrs={'class': 'details', 'id': 'jobtitle', 'placeholder': 'Enter job category (e.g. Human Ressource)'}),
            'joblocation': forms.TextInput(attrs={'class': 'details', 'id': 'joblocation', 'placeholder': 'Enter job location (e.g. Pune, INDIA )'}),
            'companyname': forms.TextInput(attrs={'class': 'details', 'id': 'companyname', 'placeholder': 'Enter company name'}),
            'jobtype': forms.TextInput(attrs={'class': 'details', 'id': 'jobtype', 'placeholder': 'Enter job type (e.g. Full-time)'}),
            'industry': forms.TextInput(attrs={'class': 'details', 'id': 'industry', 'placeholder': 'Enter industry (e.g. Healthcare Industry)'}),
            'skills': forms.TextInput(attrs={'class': 'details', 'id': 'skills', 'placeholder': 'Enter required skills (comma-separated)'}),
            'description': forms.Textarea(attrs={'class': 'details', 'id': 'description', 'placeholder': 'Enter job description'}),
            'qualification': forms.TextInput(attrs={'class': 'details', 'id': 'qualification', 'placeholder': 'Enter required qualification'}),
            'experience': forms.TextInput(attrs={'class': 'details', 'id': 'experience', 'placeholder': 'Enter required experience (e.g. 2 years)'}),
            'salary': forms.TextInput(attrs={'class': 'details', 'id': 'salary', 'placeholder': 'Enter salary range (e.g. $50,000 - $70,000/per month )'}),
            'url': forms.URLInput(attrs={'class': 'details', 'id': 'url', 'placeholder': 'Enter company website'}),
            'email': forms.EmailInput(attrs={'class': 'details', 'id': 'email', 'placeholder': 'Enter contact email'}),
            'linkedin': forms.URLInput(attrs={'class': 'details', 'id': 'linkedin', 'placeholder': 'Enter LinkedIn profile URL'}),
        }
