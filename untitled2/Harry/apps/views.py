from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("This is home of app");
def item(request):
    return HttpResponse("This is item");