from django.shortcuts import render
from .forms import Jobform

# Create your views here.
def jobposting(request):
    if request.method=="POST":
        fm=Jobform(request.POST)
        if fm.is_valid():
            fm.save()
        fm=Jobform()
    else:
      fm=Jobform()
    return render(request,'jobpost/jobpost.html',{"form":fm})
