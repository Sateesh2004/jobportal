from django.shortcuts import render
from jobpost.models import Job
# Create your views here.
def jobshowing(request):
    job = Job.objects.all()
    return render(request,'joblist/joblist.html',{'job':job})