from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.


def HomePage(request):
    return render(request, "index.html")


def SignupPage(request):
    if request.method =="POST":
        Username = request.POST['Username']       
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        myuser= User.objects.create_user(Username, email, password1)
        myuser.first_name =firstname
        myuser.last_name= lastname
        
        myuser.save()
        
        
        messages.success(request, "Your account is created succesfully")
        return render('LoginPage')
    
    return render(request, "SignupPage.html")

#https://www.youtube.com/watch?v=1UvTNMH7zDo&list=LL&index=2&t=895s&ab_channel=GeeksforGeeks
#30:41

def LoginPage(request):
    return render(request, "LoginPage.html")


def ResetPasswordPage(request):
    return render(request, "ResetPasswordPage.html")
    

def SingOut(request):
    pass
    

    