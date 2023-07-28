from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Sample

# Create your views here.


def index(request):
    sample=Sample.objects.all()
    return render(request,'index.html',{'sample':sample})



def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        if password==password1:
            reg=User.objects.create_user(username=username,password=password)
            reg.save();
            return render(request,'login.html')
        else:
            messages.info(request,'The password is not matching please try again later')
            return redirect('register')
    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('page.html')
        else:
            messages.info(request,'invalid username or password')
    return render(request,'login.html')


def form(request):
    return render(request,'form.html')