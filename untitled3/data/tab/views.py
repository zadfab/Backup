from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import student
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import student


# Create your views here.
def default(request):
    return render(request, "default.html")


def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        date = request.POST['date']
        if pass1 == pass2:
            if User.objects.filter(username=name).exists():
                messages.info(request, "user name already exist")
                return render(request, "default.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return render(request, "default.html")
            else:
                user = User.objects.create_user(username=name, password=pass1, email=email)
                user.save()
                messages.info(request, "SIGN UP successfully done")
                param = {'name': name}
                return render(request, 'home.html', param)


        else:
            messages.info(request, "Password mismatch")
            return render(request, "default.html")

    else:
        return render(request, "default.html")


def login(request):
    if request.method == "POST":
        u = request.POST['user']
        p = request.POST['pass']
        agrr = auth.authenticate(username=u, password=p)

        if agrr is not None:
            print('hello')
            auth.login(request, agrr)
            messages.info(request, "login confirm")
            return render(request, "login.html")
        else:
            messages.info(request, "ENter correct information ")
            return render(request, "home.html")
        return render(request, "login.html")
    else:
        messages.info(request, " not a post methon")
        return render(request, "login.html")


def next(request):
    # name=request.GET.get('name')
    # rlnm=request.GET.get('mobile')
    # fee=request.GET.get('qualification')
    # mytab=tab(stdudentname=name,studentno=rlnm,stdfee=fee)
    # mytab.save();

    return HttpResponse("YOUR data STored in database")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.info(request, " User Logout Successfully")
        return render(request, "default.html")

    else:
        return redirect("/")
