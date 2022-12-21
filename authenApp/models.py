from django.db import models


class TrainingPrograms(models.Model):
    programName = models.CharField(max_length=100)
    programDifficulty = models.CharField(max_length=2)
    programTrainer = models.CharField(max_length=100)
    programType = models.CharField(max_length=100)
    programDescription = models.CharField(max_length=100)

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
    start_date = models.DateField()
    end_date = models.DateField()

    # @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.Profile.save()
