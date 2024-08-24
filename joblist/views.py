
from django.shortcuts import render,HttpResponseRedirect
from jobpost.models import Job
# Create your views here.
def jobshowing(request):
    if request.user.is_authenticated:
          job = Job.objects.all()
          marketing_jobs_count = Job.objects.filter(jobtitle='Marketing').count()
          customer_jobs_count = Job.objects.filter(jobtitle='Customer Service').count()
          human_jobs_count = Job.objects.filter(jobtitle='Human Resource').count()
          management_jobs_count = Job.objects.filter(jobtitle='Project Management').count()
          design_jobs_count = Job.objects.filter(jobtitle='Design & Creative').count()
          teaching_jobs_count = Job.objects.filter(jobtitle='Teaching & Education').count()
          sales_jobs_count = Job.objects.filter(jobtitle='Sales & Communication').count()
          development_jobs_count = Job.objects.filter(jobtitle='Business Development').count()
          return render(request,'joblist/joblist.html', {
        'marketing_jobs_count': marketing_jobs_count,
        'customer_jobs_count': customer_jobs_count,
        'human_jobs_count': human_jobs_count,
        'management_jobs_count': management_jobs_count,
        'design_jobs_count': design_jobs_count,
        'teaching_jobs_count': teaching_jobs_count,
        'sales_jobs_count': sales_jobs_count,
        'development_jobs_count': development_jobs_count
    })
    else:
     return HttpResponseRedirect('/sign-in/')

    

