from django.contrib import admin
from .models import Job
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display=('jobtitle', 'joblocation', 'companyname', 'jobtype', 'industry', 'description', 'skills', 'qualification', 'experience', 'salary', 'url', 'email', 'linkedin')
admin.site.register(Job,JobAdmin)