from django.db import models

# Create your models here.
class Job(models.Model):
    jobtitle = models.CharField(max_length=50)
    joblocation = models.CharField(max_length=50)
    companyname = models.CharField(max_length=50)
    jobtype = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    skills = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    experience=models.CharField(max_length=30)
    salary=models.CharField(max_length=30)
    url=models.CharField(max_length=30)
    email=models.EmailField()
    linkedin=models.CharField(max_length=30)
    
    
