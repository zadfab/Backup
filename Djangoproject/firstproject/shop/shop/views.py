from django.http import HttpResponse
from django.shortcuts import render
def indexshop(request):
    return HttpResponse('Hello shop');

def product(request):
        return HttpResponse('My product');
def credit(request):

    return render(request,"new1.html")