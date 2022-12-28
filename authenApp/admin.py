from django.contrib import admin
from .models import TrainingPrograms, Profile, Schedule
from embed_video.admin import AdminVideoMixin
from .models import Videoss


# Register your models here.
admin.site.register(TrainingPrograms)

admin.site.register(Profile)


admin.site.register(Schedule)




#videos
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Videoss, MyModelAdmin)