from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from duty.models import *
def base(request):
    return render(request,"base.html")
def index(request):
    return render(request,"index.html")
def Adminlogin(request):
    if request.method=="POST":
        data=request.POST
        username=data.get("username")
        password=data.get("password")
        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username")
            return redirect("/Adminlogin/")

        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,"Invalid Password")
            return redirect("/Adminlogin/")
        else:
            login(request,user)
            return redirect("/AdminloginAction/")
    
    return render(request,"Adminlogin.html",)

def Adminregister(request):
    if request.method=="POST":
        data=request.POST
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        username=data.get('username')
        password=data.get('password')
        
        user=User.objects.filter(username=username)
        if user.exists():
            messages.error(request,"username already taken")
            return redirect("/Adminregister/")
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.info(request,"Account Created Successfully")
        return redirect("/Adminregister/")
        


    return render(request,"Adminregister.html")
def AdminloginAction(request):
    
    return render(request,"AdminloginAction.html")
def AddFaculty_page(request):
    if request.method=="POST":
        data=request.POST
        faculty_name=data.get('faculty_name')
        gender=data.get('gender')
        contact=data.get('contact')
        qualification=data.get('qualification')
        username=data.get('username')
        password=data.get('password')

        AddFaculty.objects.create(
            faculty_name=faculty_name,
            gender=gender,
            contact=contact,
            qualification=qualification,
            username=username,
            password=password
        )

        
        messages.success(request,"Faculty Added Successfully")
        return redirect("/AddFaculty/")

    queryset=AddFaculty.objects.all()
    context={'queryset':queryset}
    return render(request,"AddFaculty.html",context)
def ScheduleExam(request):
    if request.method == "POST":
        data=request.POST
        examname=data.get("examname")
        hall=data.get("hall")
        examtime=data.get("examtime")
        examdate=data.get("examdate")

        Schedule.objects.create(
            examname=examname,
            hall=hall,
            examtime=examtime,
            examdate=examdate,   
        )
        messages.success(request,"Added Successfully")
        return redirect("/ScheduleExam/")
    return render(request,"ScheduleExam.html")
def AddLeisure(request):
    queryset=AddFaculty.objects.all()
    context={'queryset':queryset}
    return render(request,"AddLeisure.html",context)
def available(request):
    return redirect(request,"available_faculty.html")