from django.shortcuts import render
from jobpost.models import Job
# Create your views here.
def marketingjobshowing(request):
    marketing_jobs = Job.objects.filter(jobtitle='Marketing')
    return render(request, 'marketing/marketing.html', {'marketing_jobs': marketing_jobs})
