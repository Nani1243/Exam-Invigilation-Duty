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
        username=data.get('username')
        password=data.get('password')
        
        user=User.objects.filter(username=username)
        if user.exists():
            messages.warning(request,"username already taken")
            return redirect("/Adminregister/")
        
        user=User.objects.create(
            first_name=first_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.success(request,"Account Created Successfully")
        return redirect("/Adminregister/")
        


    return render(request,"Adminregister.html")
@login_required(login_url="Adminlogin")
def AdminloginAction(request):
    
    return render(request,"AdminloginAction.html")
@login_required(login_url="Adminlogin")
def AddFaculty_page(request):
    if not request.user.is_authenticated:
       
        return redirect('/Adminlogin/')
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
@login_required(login_url="Adminlogin")
def available_faculty(request):
    return render(request,"available_faculty.html")
@login_required(login_url="Adminlogin")
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
        
        try:
            faculty=AddFaculty.objects.get(faculty_name__icontains=facultyname1)
            print(facultyname1)
        except AddFaculty.DoesNotExist:
            messages.error(request,"faculty not found")
            return redirect("ScheduleExam")
            
        s=Schedule(
            examname=examname,
            hall=hall,
            examtime=examtime,
            examdate=examdate,
            facultyname1=faculty
        )
        s.save()
        return redirect("/AfterSchedule/")
    queryset=AddLeisurepage.objects.all()
    context={'queryset':queryset}
    return render(request,"ScheduleExam.html",context)
@login_required(login_url="Adminlogin")
def AddLeisure(request):
    if request.method=="POST":
        data=request.POST
        
        facultyname=data.get('facultyname')
        examtime=data.get('examtime')
        

        
        try:
            faculty=AddFaculty.objects.get(faculty_name__icontains=facultyname)
            

        except AddFaculty.DoesNotExist:
            messages.error(request,"faculty not found")
            return redirect("AddLeisure")
            
        a=AddLeisurepage(facultyname=faculty,examtime=examtime)
        a.save()
        messages.success(request,f"{examtime} Alloted to {faculty}")
    queryset=AddFaculty.objects.all()
            
    context={'queryset':queryset}
    return render(request,"AddLeisure.html",context)
@login_required(login_url="Adminlogin")
def AfterSchedule(request):
    queryset=AddLeisurepage.objects.all()
    
    context={"queryset":queryset}
    return render(request,"AfterSchedule.html",context)
def confirm(request,facultyname):
    res=''
    print(facultyname)
    
    
   
    try:
        q=Schedule.objects.all().last()
        if not q.facultyname1.faculty_name == facultyname:
            q.delete()
            messages.error(request,"selected wrong faculty")
            return redirect("ScheduleExam")
        else:
            res=Schedule.objects.all().last()
       
    except Exception as e:
        print(e)


    context={'q':res,'faculty':facultyname}
    return render(request,"confirm.html",context)
@login_required(login_url="Adminlogin")
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

        try:

            facul=AddFaculty.objects.get(username__icontains=user)
            faculty_name=facul.faculty_name
            pas=AddFaculty.objects.get(password__icontains=password1)

            if facul and pas:
                return redirect("invigilatorpage",res=faculty_name)
            else:
                messages.error(request,"Invalid Credentials")
                return redirect("/invigilator/")
        except AddFaculty.MultipleObjectsReturned:
            messages.error(request,"Multiple uses found. Plese provide specific credentials")
            return redirect("/invigilator/")
        except AddFaculty.DoesNotExist:
            messages.error(request,"Invalid Credentials")
            return redirect('invigilator')

    
    return render(request,"invigilator.html")

def invigilatorpage(request,res):
    res=res
    
    return render(request,"invigilatorpage.html",{'res':res})

def invigilatorAllot(request,faculty_name):
    queryset=Schedule.objects.filter(facultyname1__faculty_name__icontains=faculty_name)
    context={'queryset':queryset}
    return render(request,"invigilatorAllot.html",context)
def logout_page(request):
    logout(request)
    return redirect("/index/")