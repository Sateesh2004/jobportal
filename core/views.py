from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .forms import EditUserProfileForm
from jobpost.models import Job
# Create your views here.
def home(request):
    marketing_jobs_count = Job.objects.filter(jobtitle='Marketing').count()
    customer_jobs_count = Job.objects.filter(jobtitle='Customer Service').count()
    human_jobs_count = Job.objects.filter(jobtitle='Human Resource').count()
    management_jobs_count = Job.objects.filter(jobtitle='Project Management').count()
    design_jobs_count = Job.objects.filter(jobtitle='Design & Creative').count()
    teaching_jobs_count = Job.objects.filter(jobtitle='Teaching & Education').count()
    sales_jobs_count = Job.objects.filter(jobtitle='Sales & Communication').count()
    development_jobs_count = Job.objects.filter(jobtitle='Business Development').count()

    return render(request, "core/index.html", {
        'marketing_jobs_count': marketing_jobs_count,
        'customer_jobs_count': customer_jobs_count,
        'human_jobs_count': human_jobs_count,
        'management_jobs_count': management_jobs_count,
        'design_jobs_count': design_jobs_count,
        'teaching_jobs_count': teaching_jobs_count,
        'sales_jobs_count': sales_jobs_count,
        'development_jobs_count': development_jobs_count
    })
def about(request):
    return render(request,"core/about.html")
def profile(request):
 if request.user.is_authenticated:
    user=request.user
    first_name=user.first_name
    last_name=user.last_name
    username=user.username
    first_letter=user.username[0]
    email=user.email
    return render(request, 'core/profile.html',{'first_name': first_name, 'last_name': last_name,'user_name':username,'email':email,'dp':first_letter})
 else:
     return HttpResponseRedirect('/sign-in/')
def editprofile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Profile updated successfully.')
                
        else:
            fm = EditUserProfileForm(instance=request.user)
        return render(request, 'core/editprofile.html', {'form': fm})
    else:
        return HttpResponseRedirect('/sign-in/')


