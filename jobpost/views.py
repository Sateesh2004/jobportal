from django.shortcuts import render,HttpResponseRedirect
from .forms import Jobform
from django.contrib import messages
# Create your views here.
def jobposting(request):
    if request.user.is_authenticated:
       if request.method=="POST":
        fm=Jobform(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'You have successfully posted a job.')
        fm=Jobform()
       else:
         fm=Jobform()
       return render(request,'jobpost/jobpost.html',{"form":fm})
    else:
     return HttpResponseRedirect('/sign-in/')
