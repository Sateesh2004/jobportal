
from .forms import SeekerForm

from django.shortcuts import render,HttpResponseRedirect
def register_user(request):
 if request.user.is_authenticated:
    if request.method == 'POST':
        form = SeekerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = SeekerForm()
            
    else:
        form = SeekerForm()
    return render(request, 'apply/apply.html', {'form': form})
 else:
     return HttpResponseRedirect('/sign-in/')
