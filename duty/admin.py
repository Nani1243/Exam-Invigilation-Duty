from django.contrib import admin
from .models import *

admin.site.register(AddFaculty)
class ScheduleAdmin(admin.ModelAdmin):
    list_display=['facultyname1','examname','hall','examdate']
admin.site.register(Schedule,ScheduleAdmin)
admin.site.register(AddLeisurepage)
