from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse("<h style='color:red;font-size:100px;'>Hello world<h>");
def login(request):
    return render(request,'loginpage.html');


def wel(request):
    nm=request.GET.get('name','default');
    pw=request.GET.get('password','default');
    print((nm,pw) )
    param={'nam':nm,'pas':pw}
    return render(request,'welcome.html',param);