from django.shortcuts import render
from django.http import HttpResponse
from .models import student
# Create your views here.

def homepage(request):
    return render(request,"Entry_page.html")

def result(request):
    first_name = request.GET.get("first")
    last_name = request.GET.get("last")
    school_name = request.GET.get("school")
    rollno = request.GET.get("rollno")
    phoneno = request.GET.get("phoneno")
    email = request.GET.get("email")
    name = first_name+" "+last_name
    param ={"name":name,"school_name":school_name,"rollno":rollno,"phoneno":phoneno,"email":email}
    try:
        data = student(name = name ,rollno = rollno,school_name = school_name,phoneno = phoneno, email = email)
        data.save()
    except:
        return render(request,"existed_error.html")
    return render(request,"result.html",param)

def update(request):
    return render(request,"update.html")

def confirm(request):

    first_name = request.GET.get("first")
    last_name = request.GET.get("last")
    school_name = request.GET.get("school")
    rollno = request.GET.get("rollno")
    phoneno = request.GET.get("phoneno")
    email = request.GET.get("email")
    name = first_name+" "+last_name
    try:
        filtered_value = student.objects.get(rollno = rollno )
    except:
        return render(request,"Not_exist.html")

    x = [[i.name,i.rollno,i.email] for i in student.objects.all()]
    for i in student.objects.all().values_list('name','email'):
        print(i)
    print(x)
    filtered_value.name = name
    filtered_value.rollno = rollno
    filtered_value.school_name = school_name
    filtered_value.phoneno = phoneno
    filtered_value.email = email
    filtered_value.save()
    param = {"name":name,"rollno":rollno,"school_name":school_name,"phoneno":phoneno,"email":email}
    return render(request,"updated.html",param)

def dashboard(request):
    return render(request,"design/index.html")