from django import forms
from .models import Trainers
from django import forms
from django.contrib.auth.forms import UserCreationForm
from authenApp.models import User


class TrainingProgramForm(forms.Form):
    program_name = forms.CharField(max_length=100)
    program_difficulty = forms.CharField(max_length=2)
    program_type = forms.CharField(max_length=100)
    program_description = forms.CharField(max_length=100)
    trainers = forms.ModelMultipleChoiceField(queryset=Trainers.objects.all(), widget=forms.CheckboxSelectMultiple)





class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]