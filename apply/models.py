from django.db import models
# Create your models here.
class Seekers(models.Model):
    user_name=models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, null=True, blank=True)
    resume = models.FileField(upload_to='resumes/')
    education = models.TextField()
    work_experience = models.TextField()
    skills = models.TextField()
    portfolio = models.URLField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    github_profile = models.URLField(blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)