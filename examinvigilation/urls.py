"""
URL configuration for examinvigilation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from duty.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("base/",base,name='base'),
    path("index/",index,name='index'),
    path("Adminlogin/",Adminlogin,name='Adminlogin'),
    path("Adminregister/",Adminregister,name='Adminregister'),
    path("AdminloginAction/",AdminloginAction,name='AdminloginAction'),
    path("AddFaculty/",AddFaculty_page,name='AddFaculty'),
    path("ScheduleExam/",ScheduleExam,name='ScheduleExam'),
    path("AddLeisure/",AddLeisure,name='AddLeisure'),
    path("available_faculty/",available_faculty,name="available"),
    path("AfterSchedule/",AfterSchedule,name='AfterSchedule'),
    path("confirm/<facultyname>",confirm,name='confirm'),
    path("ViewSchedule/",ViewSchedule,name='ViewSchedule'),
    path("invigilator/",invigilator,name='invigilator'),
    path("invigilatorpage/<res>",invigilatorpage,name='invigilatorpage'), 
    path("invigilatorAllot/<faculty_name>",invigilatorAllot,name='invigilatorAllot'),           
]
