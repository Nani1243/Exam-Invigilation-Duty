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
class Schedule(models.Model):
    examname=models.CharField(max_length=100)
    hall=models.IntegerField()
    Exam=(('9AM-12PM','9AM-12PM'),('10AM-13PM','10AM-13PM'),('11AM-14PM','11AM-14PM'),('12PM-15PM','12PM-15PM'),('13PM - 16PM','13PM - 16PM'),('14PM - 17PM','14PM - 17PM'),('15PM - 16PM','15PM - 16PM'))
    examtime=models.CharField(max_length=100,choices=Exam)
    examdate=models.DateField()
    facultyname1=models.CharField(max_length=100)

    def __str__(self)->str:
        return self.examname
class AddLeisurepage(models.Model): 
    
    facultyname=models.CharField(max_length=100)
    Exam=(('9AM-12PM','9AM-12PM'),('10AM-13PM','10AM-13PM'),('11AM-14PM','11AM-14PM'),('12PM-15PM','12PM-15PM'),('13PM - 16PM','13PM - 16PM'),('14PM - 17PM','14PM - 17PM'),('15PM - 16PM','15PM - 16PM'))
    examtime=models.CharField(max_length=100,choices=Exam)
    def __str__(self)->str:
        return self.facultyname
