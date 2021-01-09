from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import studentcomment, student


# Create your views here.
def sos(request):
    return render(request, 'home.html')


def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        rollno = request.POST['rollno']
        email = request.POST['email']
        course = request.POST['course']
        address = request.POST['address']
        city = request.POST['city']
        year = request.POST['year']
        comment = request.POST['comment']

        if len(name) >= 3:
            stud = student(name=name, rollno=rollno, email=email, course=course, address=address, city=city, year=year)
            comm = studentcomment(comment=comment)
            stud.save();
            comm.save();

        param = {'webname': name, 'webroll': rollno, 'comment': comment}
        return render(request, 'display.html', param)
    else:
        return HttpResponse('something went wrong')


def info(request):
    if request.method == "POST":
        obj = student.objects.all()

        obj1 = studentcomment.objects.all()
        param = {'obj': obj, 'obj1': obj1}

        return render(request, 'info.html', param)


def product(request, id):
    #  glue=student.objects.get(id=id)
    glue = get_object_or_404(student, id=id)
    param = {'glue': glue}
    if request.method == "POST":
        glue.delete()
        return redirect("../../")

    return render(request, "dynamicur.html", param)
