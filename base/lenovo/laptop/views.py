from django.shortcuts import render
from django.http import HttpResponse
from .models import student
# Create your views here.
def home(request):
    return render(request,'default.html')

def success(request):
    name=request.GET.get('name')
    roll=request.GET.get('roll')

    datbas=student(stdname=name,rollno=roll)
    datbas.save()


    return HttpResponse("DATA SAVED IN DATABASE")