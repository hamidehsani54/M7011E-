
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
from .models import TrainingPrograms

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
        message = "Hello"+ myuser.first_name  + "!! \n" + "Welcome to Your Personal Trainer and we are glad to have you here! \nYour account has been created! \n\n Thank You\n Hamid Ehsani"
        from_email = settings.EMAIL_HOST_USER
        auth_user = settings.EMAIL_HOST_USER
        auth_password= settings.EMAIL_HOST_PASSWORD

        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently = False, auth_user=auth_user, auth_password=auth_password)



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
            messages.error(request, "Username or password is incorrect!")
            return redirect('LoginPage')

    return render(request, "LoginPage.html")



def SignOut(request):
    logout(request)
    messages.success(request, "Your are loged out now")
    return redirect("HomePage")
def Profile(request):
    return render(request, "Profile.html")


def About(request):
    return render(request, "About.html")


def Contact(request):
    return render(request, "Contact.html")


def Back(request):
    return render(request, "Exercises/back.html")


def Chest(request):
    return render(request, "Exercises/chest.html")


def Arms(request):
    return render(request, "Exercises/arms.html")


def Leg(request):
    return render(request, "Exercises/leg.html")


def Shoulder(request):
    return render(request, "Exercises/shoulder.html")


def CalorieCalc(request):
    if request.method == 'POST':
        weight = int(request.POST.get('weight'))
        height = int(request.POST.get('height'))
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')
        activity_level = request.POST.get('activity_level')

        if gender == 'male':
            BMR = 66.5 + (13.8 * weight) + (5 * height) - (6.8 * age)
        else:
            BMR = 655.1 + (9.6 * weight) + (1.9 * height) - (4.7 * age)

        if activity_level == 'sedentary':
            BMR = BMR * 1.2
        elif activity_level == 'light':
            BMR = BMR * 1.375
        elif activity_level == 'moderate':
            BMR = BMR * 1.55
        elif activity_level == 'heavy':
            BMR = BMR * 1.1725
        elif activity_level == 'very_heavy':
            BMR = BMR * 1.9

        return render(request, 'CalorieCalc.html', {'daily_caloric_intake': BMR})

    return render(request, 'CalorieCalc.html')


def Subscribe1(request):
    return render(request, "Subscribe.html")


def Subscribe(request):
    #  TESTING (looks like it works as intended)
    #  THIS SHOULD BE IMPLEMENTED ELSEWHERE

    TrainingPrograms.objects.create(programName="Test1",
                                    programDifficulty='6',
                                    programTrainer="Folke",
                                    programDescription="upperbody and core",
                                    programType="low Volume lifting")

    #  END TESTING
    entries = TrainingPrograms.objects.all()
    try:
        current_user = User.objects.get(pk=request.user.id)
        current_user_logged = current_user.is_authenticated

        # Get the current user's profile
        #profile, created = Profile.objects.get_or_create(user=request.user)

        # Update the user's program field


    except User.DoesNotExist:
        current_user_logged = False

    if current_user_logged:
        # User is logged in, display a welcome message
        #current_user.program = 'My Program'
        #current_user.save()

        #current_user.ExtendedUser.objects.set(program='123')
        ## TODO: This part should take post and update OneToOneField.program to include the program.
        #subscribeTo = request.POST.get['button']
        print(current_user.program)
        print("TEST BEFORE")
        current_user.program = "testtest"
        current_user.save()
        print(current_user.program)
        print("AFTER TEST")

        return render(request, "Subscribe.html", {'entries': entries})
    else:
        # User is not logged in, display a login prompt
        return render(request, "LoginPage.html")
