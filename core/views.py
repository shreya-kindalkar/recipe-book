from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method=="POST":
        username=request.POST['email']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        
        if password!=confirmpassword:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request,"User already exists.")
            return redirect('signup')
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        messages.success(request,"Account created")
        return redirect('login')
    return render(request,"core/signup.html")
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(request,username=email,password=password)
        if user:
            login(request,user)
            return redirect ('dashboard')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')
    return render(request, 'core/login.html')