from django.db import models
from django.contrib.auth.models import User


class TrainingPrograms(models.Model):
    programName = models.CharField(max_length=100)
    programDifficulty = models.CharField(max_length=2)
    programTrainer = models.CharField(max_length=100)
    programType = models.CharField(max_length=100)
    programDescription = models.CharField(max_length=100)


class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    program = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()


#@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ExtendedUser.objects.create(user=instance)


#@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.ExtendedUser.save()
