from django import forms
from .models import Trainers


class TrainingProgramForm(forms.Form):
    program_name = forms.CharField(max_length=100)
    program_difficulty = forms.CharField(max_length=2)
    program_type = forms.CharField(max_length=100)
    program_description = forms.CharField(max_length=100)
    trainers = forms.ModelMultipleChoiceField(queryset=Trainers.objects.all(), widget=forms.CheckboxSelectMultiple)
