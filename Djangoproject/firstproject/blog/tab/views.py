from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def default(request):
    return render(request, "default.html")


def home(request):
    return render(request, "home.html")


def next(request):
    return HttpResponse("YOUR data STored in database")


