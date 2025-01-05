from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
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
        messages.successs(request,"Account Created Successfully")
        return redirect("/Adminregister/")
        


    return render(request,"Adminregister.html")
@login_required
def AdminloginAction(request):
    
    return render(request,"AdminloginAction.html")
@login_required
def AddFaculty_page(request):
    if request.method=="POST":
        data=request.POST
        faculty_name=data.get('faculty_name')
        gender=data.get('gender')
        contact=data.get('contact')
        qualification=data.get('qualification')
        username=data.get('username')
        password=data.get('password')
        
        user1=AddFaculty.objects.filter(username=username)
        if user1.exists():
            messages.error(request,"username already exists")
            return redirect("/AddFaculty/")


        user=AddFaculty.objects.create(
            faculty_name=faculty_name,
            gender=gender,
            contact=contact,
            qualification=qualification,
            username=username,
            password=password,
        )
        
        
        messages.success(request,"Faculty Added Successfully")
        return redirect("/AddFaculty/")
    queryset=AddFaculty.objects.all()
    context={'queryset':queryset}
    return render(request,"AddFaculty.html",context)
@login_required
def available_faculty(request):
    return render(request,"available_faculty.html")
def ScheduleExam(request):
    if request.method == "POST":
        data=request.POST
        examname=data.get("examname")
        hall=data.get("hall")
        examtime=data.get("examtime")
        examdate=data.get("examdate")
        facultyname1=data.get("facultyname1")
        

        user=Schedule.objects.filter(examname=examname)
        if user.exists():
            messages.error(request,"This Subject Already Taken")
            return redirect("/ScheduleExam/")

        Schedule.objects.create(
            examname=examname,
            hall=hall,
            examtime=examtime,
            examdate=examdate,
            facultyname1=facultyname1   
        )
        return redirect("/AfterSchedule/")
    queryset=AddFaculty.objects.all()
    context={'queryset':queryset}
    return render(request,"ScheduleExam.html",context)
@login_required
def AddLeisure(request):
    if request.method=="POST":
        data=request.POST
        facultyname=data.get('facultyname')
        examtime=data.get('examtime')

        AddLeisurepage.objects.create(
            facultyname=facultyname,
            examtime=examtime
        )
        add=AddLeisurepage.objects.filter(facultyname__icontains=facultyname)
        for a in add:
            messages.info(request,f"{a.examtime} is alloted to {a.facultyname}")
    queryset=AddFaculty.objects.all()
    context={'queryset':queryset}
    return render(request,"AddLeisure.html",context)
@login_required
def AfterSchedule(request):
    queryset=AddLeisurepage.objects.all()
    context={"queryset":queryset}
    return render(request,"AfterSchedule.html",context)
def confirm(request,facultyname):
    queryset=Schedule.objects.filter(facultyname1__icontains=facultyname)
    
    context={'queryset':queryset}
    return render(request,"confirm.html",context)
@login_required
def ViewSchedule(request):
    queryset=Schedule.objects.all()
    context={"queryset":queryset}

    return render(request,"ViewSchedule.html",context)

def invigilator(request):
    res=""
    if request.method== "POST":
        data=request.POST
        user=data.get("user")
        password1=data.get("password1")

        

        facul=AddFaculty.objects.get(username__icontains=user)
        faculty_name=facul.faculty_name
    
        return redirect("invigilatorpage",res=faculty_name)

    
    return render(request,"invigilator.html")

def invigilatorpage(request,res):
    res=res
    
    return render(request,"invigilatorpage.html",{'res':res})


def invigilatorAllot(request,faculty_name):
    queryset=Schedule.objects.filter(facultyname1__icontains=faculty_name)
    context={'queryset':queryset}
    return render(request,"invigilatorAllot.html",context)