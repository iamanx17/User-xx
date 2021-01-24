from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                note=False
                messages.info(request,'Username is already taken')
                return render(request,'result.html',{'res':note})
                
            elif User.objects.filter(email=email).exists():
                note=False
                messages.info(request,'Email is already taken')
                return render(request, 'result.html',{'res':note})
        
            else:   
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                note=True
                messages.info(request,'User has been created successfully!!')
                return render(request,'result.html',{'res':note})
                
        else:
            messages.info(request,'Password not matched!!')
            note=False
            return render(request,'result.html',{'res':note})
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('login')
        else:
            messages(request,'User not found')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')