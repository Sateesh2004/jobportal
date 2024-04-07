from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm
from .forms import CustomAuthenticationForm
from django.contrib.auth import authenticate,login,logout
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sign-in/')
            
    else:
        form = SignUpForm()
    return render(request, 'enroll/sign_up.html', {'form': form})
def sign_in(request):
  if request.method == 'POST':
    fm = CustomAuthenticationForm(request=request,data=request.POST)
    if fm.is_valid():
        uname=fm.cleaned_data['username']
        upass=fm.cleaned_data['password']
        user = authenticate(username=uname,password=upass)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/home/')
  else:
        fm=CustomAuthenticationForm()
  return render(request,'enroll/sign_in.html',{'form':fm})    
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/sign-in/')
