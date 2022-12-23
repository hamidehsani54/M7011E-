from django.db import models
from django.contrib.auth.models import User, Group


class Schedule(models.Model):
    day = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    # Other fields for the schedule


class TrainingPrograms(models.Model):
    programName = models.CharField(max_length=100)
    programDifficulty = models.CharField(max_length=2)
    programTrainer = models.CharField(max_length=100)
    programType = models.CharField(max_length=100)
    programDescription = models.CharField(max_length=100)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True)

class schudle(models.Model):
    Monday =models.CharField(max_length=100)
    Tuesday =models.CharField(max_length=100)
    Wednesday =models.CharField(max_length=100)
    Thursday =models.CharField(max_length=100)
    Friday =models.CharField(max_length=100)
    Saturday =models.CharField(max_length=100)
    Sunday =models.CharField(max_length=100)
    
class Profile(models.Model):

    program = models.CharField(max_length=100, blank=True)


class User(models.Model):
    # other fields here
    groups = models.ManyToManyField(Group, related_name='users', blank=True)
