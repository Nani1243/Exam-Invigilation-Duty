from django.db import models
from django.contrib.auth.models import User
class Duty(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
class AddFaculty(models.Model):
    faculty_name=models.CharField(max_length=100)
    Gender_choices=(('M','Male'),
       ('F','Female'),
       ('O','Others'))
    qualification_choices=(('M','M.TECH'),
       ('M','MBA'),('M','MCA'),('M','MSC'),('D','DEGREE'),('B','BTECH')
       )
    gender=models.CharField(max_length=100,choices=Gender_choices,default="Male")
    contact=models.CharField(max_length=100,default="")
    qualification=models.CharField(max_length=100,choices=qualification_choices,default="M.TECH")
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self)->str:
        return self.faculty_name
