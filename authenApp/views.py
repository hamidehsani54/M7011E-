from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from .models import TrainingPrograms, Schedule, Video, Trainers
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from website import settings
from django.views import generic
from django.urls import reverse_lazy
from .forms import TrainingProgramForm


def is_member_of_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
# Create your views here.


def HomePage(request):
    if is_member_of_group(request.user, 'trainer'):
        # user is a trainer render with aditional information
        # TODO: add aditional info
        return render(request, "index.html")
    else:
        return render(request, "index.html")
        # user is not a trainer


def SignupPage(request):
    if request.method == "POST":
        username = request.POST['username']
        # firstname = request.POST['firstname']
        # lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        access = request.POST['access']

        # check if username already exist
        if User.objects.filter(username=username):
            messages.error(request, "User already exist!")
            return redirect('LoginPage')

        # check if email already registred

        if User.objects.filter(email=email):
            messages.error(request, "Email already registred!")
            return redirect('LoginPage')

        # too long username
        if len(username) > 10:
            messages.error(request, "Username is too long")

        # check password 1 =password 2
        if password1 != password2:
            messages.error(request, "Passwords does not match")

        # wrong type of username input
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-numeric!")
            return redirect('HomePage')
        if len(password1) < 5:
            messages.error(request, "Please select a stronger password")

        myuser = User.objects.create_user(username, email, password1)

        if(access == 'trainer'):
            user = User.objects.get(username=username)
            trainer_group = Group.objects.get(name='trainer')
            user.groups.add(trainer_group)
            trainer = Trainers(user=user)
            trainer.save()

        #authenApp.signals.create_user_profile(sender=username)
        myuser.is_active = True
        myuser.save()

        messages.success(request, "Your account is created succesfully. Please check your email!")

        # welcome Email
        subject = "welcome To Your Personal Trainer!"
        message = "Hello" + myuser.first_name + "!! \n" + "Welcome to Your Personal Trainer and we are glad to have you here! \nYour account has been created! \n\n Thank You\n Hamid Ehsani"
        from_email = settings.EMAIL_HOST_USER
        auth_user = settings.EMAIL_HOST_USER
        auth_password = settings.EMAIL_HOST_PASSWORD

        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False, auth_user=auth_user, auth_password=auth_password)

        return render(request, 'LoginPage.html')

    return render(request, "SignupPage.html")


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)
        print(user)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, "index.html", {'firstname': firstname})
        else:
            messages.error(request, "Username or password is incorrect!")
            return redirect('LoginPage')

    return render(request, "LoginPage.html")


def SignoutPage(request):
    logout(request)
    messages.success(request, "Your are logged out now")
    return redirect("HomePage")


@login_required(login_url='LoginPage')
def Profile(request):
    current_user = User.objects.get(pk=request.user.id)
    group = Group.objects.get(name='trainer')
    usersWithGroup = User.objects.filter(groups=group)

    # Check if the user is in the group
    if current_user in usersWithGroup:
        # User is in the group
        return render(request, "Profile.html", {'trainer': True, 'name': current_user.username})
    else:
        # User is not in the group
        return render(request, "Profile.html", {'name': current_user})


def About(request):
    return render(request, "About.html")


def Contact(request):
    return render(request, "Contact.html")


def edit_profile(request):
    return render(request, "edit_profile.html")


@login_required(login_url='LoginPage')
def Back(request):
    return render(request, "Exercises/back.html")


@login_required(login_url='LoginPage')
def Chest(request):
    return render(request, "Exercises/chest.html")


@login_required(login_url='LoginPage')
def Arms(request):
    return render(request, "Exercises/arms.html")


@login_required(login_url='LoginPage')
def Leg(request):
    return render(request, "Exercises/leg.html")


@login_required(login_url='LoginPage')
def Shoulder(request):
    return render(request, "Exercises/shoulder.html")


@login_required(login_url='LoginPage')
def Videos(request):
    obj = Video.objects.all()
    return render(request, "Videos.html", {'obj': obj})


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

        return render(request, 'CalorieCalc.html',
                               {'daily_caloric_intake': BMR})
    return render(request, 'CalorieCalc.html')


def Subscribe(request):
    entries = TrainingPrograms.objects.all()
    try:
        current_user = User.objects.get(pk=request.user.id)
        current_user_logged = current_user.is_authenticated

    except User.DoesNotExist:
        current_user_logged = False

    if current_user_logged:
        if request.method == "POST":
            print("HERE")
            program = request.POST['program']
            print("program: " + program)
            current_user.profile.program = program
            current_user.profile.save()
        return render(request, "Subscribe.html", {'entries': entries})
    else:
        # User is not logged in, display a login prompt
        return render(request, "LoginPage.html")


@login_required(login_url='LoginPage')
def schedulePage(request):
    current_user = User.objects.get(pk=request.user.id)
    user_program = current_user.profile.program
    if user_program:
        program = TrainingPrograms.objects.get(programName=user_program)
        schedule = program.schedule
        print(program)
        print(schedule)
        print(schedule.day)
        print(schedule.activity)

        return render(request, 'Schedule.html', {'day': schedule.day, 'activity': schedule.activity})
    else:
        return render(request, "Profile.html", {'name': current_user})

def TrainerSiteSchedule(request):
    if request.method == "POST":
        programName = request.POST['programName']
        day = request.POST['day']
        activity = request.POST['activity']
        program = TrainingPrograms.objects.get(programName=programName)
        schedule = Schedule(day=day, activity=activity)
        schedule.save()
        program.schedule = schedule
        program.save()

    entries = TrainingPrograms.objects.all()
    return render(request, "TrainerSite.html", {'entries': entries})


def TrainerSite(request):
    if request.method == "POST":
        form = TrainingProgramForm(request.POST)
        if form.is_valid():
            # Process the form data and create a new TrainingPrograms instance
            program_name = form.cleaned_data['program_name']
            program_difficulty = form.cleaned_data['program_difficulty']
            program_type = form.cleaned_data['program_type']
            program_description = form.cleaned_data['program_description']
            trainers = form.cleaned_data['trainers']

            program = TrainingPrograms(programName=program_name,
                                       programDifficulty=program_difficulty,
                                       programType=program_type,
                                       programDescription=program_description,
                                       schedule=None)
            # Save the TrainingPrograms instance to the database
            program.save()
            # Add the many-to-many
            for trainer in trainers:
                program.trainers.add(trainer)
                program.save()
            return render(request, 'TrainerSite.html', {'form': form, 'entries': TrainingPrograms.objects.all()})
    else:
        form = TrainingProgramForm()
    return render(request, 'TrainerSite.html', {'form': form, 'entries': TrainingPrograms.objects.all()})


class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'edit_profile.html'

    success_url = reverse_lazy('edit_profile.html')

    def get_object(self):
        return self.request.user
