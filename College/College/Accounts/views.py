from django import forms
from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



# Create your views here.
def RegisterUser_view(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('LOGIN')
        else:
            messages.error(request,'Either email is alrady in use or username is taken')
    template_name='UserRegister.html'
    context={'form':form}
    return render(request,template_name,context)

def UserLogin_view(request):
    if request.method=='POST':
        u=request.POST.get('uname')
        p=request.POST.get('pword')
        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user=user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')
    template_name='UserLogin.html'
    context={}
    return render(request,template_name,context)

def UserLogout_view(request):
    logout(request)
    return redirect('LOGIN')


        


    
    