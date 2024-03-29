from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from .models import TrainingPrograms, Schedule, Video, Trainers, Exercise
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from website import settings
from django.views import generic
from django.urls import reverse_lazy
from .forms import TrainingProgramForm, SignUpForm, LoginForm, ChangeNameForm
import timeit
from django.db import connection


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
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            access = form.cleaned_data['access']
            # Check if username already exists
            if User.objects.filter(username=username):
                messages.error(request, "User already exist!")
                return redirect("LoginPage")
            # Check if email already registered
            if User.objects.filter(email=email):
                messages.error(request, "Email already registered!")
                return redirect("LoginPage")
            # Check if password1 equals password2
            if password1 != password2:
                messages.error(request, "Passwords do not match")
                return redirect("SignupPage")
            # Create user
            myuser = User.objects.create_user(username, email, password1)
            # Add user to trainer group if access is "trainer"
            if access == "trainer":
                user = User.objects.get(username=username)
                trainer_group = Group.objects.get(name="trainer")
                user.groups.add(trainer_group)
                trainer = Trainers(user=user)
                trainer.save()
            myuser.is_active = True
            myuser.save()
            messages.success(request, "Your account is created successfully. Please check your email!")
            send_welcome_email(myuser)
            return redirect("LoginPage")
    else:
        form = SignUpForm()
    return render(request, "SignupPage.html", {'form': form})


def LoginPage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Profile')
            else:
                form.add_error(None, 'Invalid login')
    else:
        form = LoginForm()
    return render(request, 'LoginPage.html', {'form': form})


def SignoutPage(request):
    logout(request)
    messages.success(request, "Your are logged out now")
    return redirect("HomePage")


@login_required(login_url='LoginPage')
def Profile(request):
    if request.method == 'POST':
        form = ChangeNameForm(request.POST)
        if form.is_valid():
            usernameNew = form.cleaned_data['usernameNew']
            usernameOld = form.cleaned_data['usernameOld']
            password = form.cleaned_data['password']
            if User.objects.filter(username=usernameNew):
                messages.error(request, "User already exist!")
                return redirect("Profile")
            user = authenticate(request, username=usernameOld, password=password)
            if user is not None:
                login(request, user)
                current_user = User.objects.get(username=usernameOld)
                current_user.username = usernameNew
                current_user.save()
                return redirect("Profile")
            else:
                form.add_error(None, 'Invalid new username')
    else:
        form = ChangeNameForm()
    current_user = User.objects.get(pk=request.user.id)
    group = Group.objects.get(name='trainer')
    usersWithGroup = User.objects.filter(groups=group)
    # Check if the user is in the group
    if current_user in usersWithGroup:
        # User is in the group
        return render(request, "Profile.html", {'trainer': True, 'name': current_user.username, 'form': form})
    else:
        return render(request, "Profile.html", {'trainer': False, 'name': current_user.username, 'form': form})


def About(request):
    return render(request, "About.html")


def Contact(request):
    return render(request, "Contact.html")


def edit_profile(request):
    return render(request, "edit_profile.html")


@login_required(login_url='LoginPage')
def Back(request):
    back_exercises = Exercise.objects.filter(exerciseType='Back')
    return render(request, "Exercises/back.html", {'exercises': back_exercises})


@login_required(login_url='LoginPage')
def Chest(request):
    chest_exercises = Exercise.objects.filter(exerciseType='Chest')
    return render(request, "Exercises/chest.html", {'exercises': chest_exercises})


@login_required(login_url='LoginPage')
def Arms(request):
    arm_exercises = Exercise.objects.filter(exerciseType='Arms')
    return render(request, "Exercises/arms.html", {'exercises': arm_exercises})


@login_required(login_url='LoginPage')
def Leg(request):
    leg_exercises = Exercise.objects.filter(exerciseType='Legs')
    return render(request, "Exercises/leg.html", {'exercises': leg_exercises})


@login_required(login_url='LoginPage')
def Shoulder(request):
    shoulder_exercises = Exercise.objects.filter(exerciseType='Shoulders')
    return render(request, "Exercises/shoulder.html", {'exercises': shoulder_exercises})


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
        schedules = program.schedules.all()
        return render(request, 'Schedule.html', {'schedules': schedules})
    else:
        return render(request, "Profile.html", {'name': current_user})


# A worse schedule page
@login_required(login_url='LoginPage')
def schedulePageBadVer(request):
    current_user = User.objects.get(pk=request.user.id)
    user_program = current_user.profile.program
    if user_program:
        program = TrainingPrograms.objects.get(programName=user_program)
        schedules = []
        for schedule in Schedule.objects.all():
            if schedule in program.schedules.all():
                schedules.append(schedule)
        return render(request, 'Schedule.html', {'schedules': schedules})
    else:
        return render(request, "Profile.html", {'name': current_user})


def TrainerSiteRemove(request):
    if request.method == "POST":
        programName = request.POST['programName']
        instance = TrainingPrograms.objects.get(programName=programName)
        instance.delete()
        TrainingPrograms.objects.filter(programName=programName).delete()
    entries = TrainingPrograms.objects.all()
    return render(request, "TrainerSite.html", {'entries': entries, 'form': TrainingProgramForm()})


def TrainerSiteSchedule(request):
    if request.method == "POST":
        programName = request.POST['programName']
        day = request.POST['day']
        activity = request.POST['activity']
        program = TrainingPrograms.objects.get(programName=programName)
        schedule = Schedule(day=day, activity=activity)
        schedule.save()
        program.schedules.add(schedule)
        program.save()

    entries = TrainingPrograms.objects.all()
    return render(request, "TrainerSite.html", {'entries': entries, 'form': TrainingProgramForm()})


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
                                       programDescription=program_description
                                       )
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


def send_welcome_email(user):
    subject = "welcome To Your Personal Trainer!"
    message = "Hello" + user.first_name + "!! \n" + "Welcome to Your Personal Trainer and we are glad to have you here! \nYour account has been created! \n\n Thank You\n Hamid Ehsani"
    from_email = settings.EMAIL_HOST_USER
    auth_user = settings.EMAIL_HOST_USER
    auth_password = settings.EMAIL_HOST_PASSWORD

    to_list = [user.email]
    send_mail(subject, message, from_email, to_list, fail_silently=False, auth_user=auth_user, auth_password=auth_password)


def authenticate_user(username, password):
    user = authenticate(username=username, password=password)
    return user


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("This username already exists")
    else:
        return HttpResponse("This username is avalible")


def check_username_login(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("")
    else:
        return HttpResponse("This user does not exist")


def check_email(request):
    email = request.POST.get('email')
    if get_user_model().objects.filter(email=email).exists():
        return HttpResponse("This email already exists")
    else:
        return HttpResponse("This email is avalible")


def check_password(request):
    password2 = request.POST.get('password2')
    password1 = request.POST.get('password1')
    if password2 == password1:
        return HttpResponse("Passwords match")
    else:
        return HttpResponse("Passwords dont match")


class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'edit_profile.html'

    success_url = reverse_lazy('edit_profile.html')

    def get_object(self):
        return self.request.user


# PERFORMANCE TESTS
# Approach 1: Get all TrainingPrograms objects, then filter
def approach1():
    programs = TrainingPrograms.objects.all()
    return programs.filter(programName='scheduleTest')


# Approach 2: Directly query TrainingPrograms objects with desired name
def approach2():
    return TrainingPrograms.objects.filter(programName='scheduleTest')


# Time how long each approach takes to execute
time1 = timeit.timeit(approach1, number=1000)
time2 = timeit.timeit(approach2, number=1000)

# Print results
print(f'Approach 1 took {time1:.5f} seconds')
print(f'Approach 2 took {time2:.5f} seconds')


# ORM vs SQL
def performanceOrmVsSql():
    # Option 1: Using raw SQL queries
    start_time = timeit.default_timer()
    print(connection.cursor())
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM authenApp_Schedule")
        rows = cursor.fetchall()
    elapsed_time = timeit.default_timer() - start_time
    print("Elapsed time using raw SQL:", elapsed_time)

    # Option 2: Using Django ORM
    start_time = timeit.default_timer()
    rows = Schedule.objects.all()
    elapsed_time = timeit.default_timer() - start_time
    print("Elapsed time using Django ORM:", elapsed_time)
    print("rows: ", len(rows))


performanceOrmVsSql()
