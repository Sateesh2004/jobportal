from django.contrib import admin
from .models import Seekers
# Register your models here.
class SeekersAdmin(admin.ModelAdmin):
    list_display=('user_name','phone_number', 'email', 'resume', 'education', 'work_experience', 'skills', 'portfolio',  'linkedin_profile', 'github_profile', 'additional_information')
admin.site.register(Seekers,SeekersAdmin)