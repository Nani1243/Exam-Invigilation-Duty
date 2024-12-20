from django.contrib import admin
from .models import *

admin.site.register(AddFaculty)
class ScheduleAdmin(admin.ModelAdmin):
    list_display=['examname','hall','examdate']
admin.site.register(Schedule,ScheduleAdmin)