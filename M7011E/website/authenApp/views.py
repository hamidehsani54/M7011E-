
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMessage, send_mail
import uuid
from telnetlib import LOGOUT

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from website import settings



# Create your views here.


def HomePage(request):
    return render(request, "index.html")


def SignupPage(request):
    if request.method =="POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

         #check if username already exist
        if User.objects.filter(username = username):
            messages.error(request, "User already exist!")
            return redirect('LoginPage')

        #check if email already registred

        if User.objects.filter(email = email):
            messages.error(request, "Email already registred!")
            return redirect('LoginPage')

        #too long username
        if len(username)>10:
            messages.error(request, "Username is too long")

        #check password 1 =password 2
        if password1 != password2:
            messages.error( request, "Passwords does not match")

        #wrong type of username input
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-numeric!")
            return redirect('HomePage')
        if len(password1)<5:
            messages.error(request, "Please select a stronger password")

        myuser= User.objects.create_user(username, email, password1)
        myuser.is_active = False
        myuser.save()


        messages.success(request, "Your account is created succesfully. Please check your email!")

        #welcome Email
        subject = "welcome To Your Personal Trainer!"
        message = "Hello"+ myuser.first_name  + "!! \n" + "Welcome to Your Personal Trainer and we are glad to have you here! \nIn order to active your account you need to confirm you our policy by clicking on the link below \n\n Thank You\n Hamid Ehsani"
        from_email = settings.EMAIL_HOST_USER
        auth_user = settings.EMAIL_HOST_USER
        auth_password = settings.EMAIL_HOST_PASSWORD
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False, auth_user=auth_user, auth_password=auth_password)



        return render(request, 'LoginPage.html')

    return render(request, "SignupPage.html")



def LoginPage(request):
    if request.method =='POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user= authenticate(username=username, password = password1)

        if user is not None:
            login(request, user)
            firstname= user.first_name
            return render(request, "index.html", {'firstname': firstname})
        else:
            messages.error(request, "uncorrect info")
            return redirect('HomePage')

    return render(request, "LoginPage.html")



def SignOut(request):
    logout(request)
    messages.success(request, "Your are loged out now")
    return redirect("HomePage")
