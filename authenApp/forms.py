from django import forms
from .models import Trainers
from django.contrib.auth.forms import UserCreationForm
from authenApp.models import User


class TrainingProgramForm(forms.Form):
    program_name = forms.CharField(max_length=100)
    program_difficulty = forms.CharField(max_length=2)
    program_type = forms.CharField(max_length=100)
    program_description = forms.CharField(max_length=100)
    trainers = forms.ModelMultipleChoiceField(queryset=Trainers.objects.all(), widget=forms.CheckboxSelectMultiple)


class SignUpForm(forms.Form):
    ACCESS_CHOICES = (
        ('trainer', 'Trainer'),
        ('user', 'User'),
        )
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    access = forms.ChoiceField(choices=ACCESS_CHOICES, widget=forms.RadioSelect)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
