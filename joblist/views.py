
from django.shortcuts import render,HttpResponseRedirect
from jobpost.models import Job
# Create your views here.
def jobshowing(request):
    if request.user.is_authenticated:
          job = Job.objects.all()
          return render(request,'joblist/joblist.html',{'job':job})
    else:
     return HttpResponseRedirect('/sign-in/')