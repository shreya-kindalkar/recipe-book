from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method=="POST":
        username=request.POST['email']
        email=request.POST['email']
        password=request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request,"User already exists.")
            return redirect('signup')
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        messages.success(request,"Account created")
        return redirect('login')
    return render(request,"signup.html")