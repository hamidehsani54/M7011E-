from django.contrib import admin
from .models import TrainingPrograms, Profile, Schedule, Trainers
from embed_video.admin import AdminVideoMixin
from .models import Video


# Register your models here.
admin.site.register(TrainingPrograms)

admin.site.register(Trainers)

admin.site.register(Profile)


admin.site.register(Schedule)


# videos
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Video, MyModelAdmin)
