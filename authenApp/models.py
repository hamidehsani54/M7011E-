from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


class Schedule(models.Model):
    day = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    # Other fields for the schedule


class Trainers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # other fields for the trainers model


class TrainingPrograms(models.Model):
    programName = models.CharField(max_length=100)
    programDifficulty = models.CharField(max_length=2)
    programType = models.CharField(max_length=100)
    programDescription = models.CharField(max_length=100)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True)
    trainers = models.ManyToManyField(Trainers, related_name='training_programs', blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    program = models.CharField(max_length=100, blank=True)


class Exercise(models.Model):
    exerciseName = models.CharField(max_length=100)
    exerciseType = models.CharField(max_length=100)
    exerciseDecription = models.CharField(max_length=100, blank=True)
    exerciseRecomendedSets = models.CharField(max_length=10)
    exerciseRecomendedReps = models.CharField(max_length=10)


# add video on the page
class Video(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
