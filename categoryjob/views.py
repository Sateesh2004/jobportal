from django.shortcuts import render,HttpResponseRedirect
from jobpost.models import Job

# Create your views here.

# Create your views here.
def customer_job_showing(request):
  if request.user.is_authenticated:
    customer_jobs = Job.objects.filter(jobtitle='Customer Service')
    return render(request, 'categoryjob/customer.html', {'customer_jobs': customer_jobs})
  else:
     return HttpResponseRedirect('/sign-in/')
def human_job_showing(request):
  if request.user.is_authenticated:
    human_jobs = Job.objects.filter(jobtitle='Human Resource')
    return render(request, 'categoryjob/human.html', {'human_jobs': human_jobs})
  else:
     return HttpResponseRedirect('/sign-in/')
def management_job_showing(request):
  if request.user.is_authenticated:
    management_jobs = Job.objects.filter(jobtitle='Project Management')
    return render(request, 'categoryjob/management.html', {'management_jobs': management_jobs})
  else:
     return HttpResponseRedirect('/sign-in/')
def development_job_showing(request):
  if request.user.is_authenticated:
    development_jobs = Job.objects.filter(jobtitle='Business Development')
    return render(request, 'categoryjob/development.html', {'development_jobs': development_jobs})
  else:
     return HttpResponseRedirect('/sign-in/')
def sales_job_showing(request):
  if request.user.is_authenticated:
    sales_jobs= Job.objects.filter(jobtitle='Sales & Communication')
    return render(request, 'categoryjob/sales.html', {'sales_jobs': sales_jobs})
  else:
     return HttpResponseRedirect('/sign-in/')
def teaching_job_showing(request):
  if request.user.is_authenticated:
    teaching_jobs = Job.objects.filter(jobtitle='Teaching & Education')
    return render(request, 'categoryjob/teaching.html', {'teaching_jobs': teaching_jobs})
  else:
     return HttpResponseRedirect('/sign-in/')
def design_job_showing(request):
  if request.user.is_authenticated:
    design_jobs = Job.objects.filter(jobtitle='Design & Creative')
    return render(request, 'categoryjob/design.html', {'design_jobs': design_jobs})
  else:
     return HttpResponseRedirect('/sign-in/')