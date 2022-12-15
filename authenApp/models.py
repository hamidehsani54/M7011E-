from django.db import models


class TrainingPrograms(models.Model):
    programName = models.CharField(max_length=100)
    programDifficulty = models.CharField(max_length=2)
    programTrainer = models.CharField(max_length=100)
    programType = models.CharField(max_length=100)
    programDescription = models.CharField(max_length=100)
