from django.contrib import admin
from .models import TrainingPrograms, Profile, Schedule
# Register your models here.
admin.site.register(TrainingPrograms)

admin.site.register(Profile)


admin.site.register(Schedule)
