from django.urls import path
from django.shortcuts import render
urlpatterns = [ path ('signup/', lambda request: render(request,'core/signup.html',{'title':'Sign Up'})),
             path ('login/',lambda request:render(request,'core/signup.html',{'title':'Login'}))]