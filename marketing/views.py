from django.shortcuts import render,HttpResponseRedirect
from jobpost.models import Job
# Create your views here.
def marketingjobshowing(request):
    if request.user.is_authenticated:
       marketing_jobs = Job.objects.filter(jobtitle='Marketing')
       return render(request, 'marketing/marketing.html', {'marketing_jobs': marketing_jobs})
    else:
       return HttpResponseRedirect('/sign-in/')