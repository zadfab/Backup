from django.shortcuts import render
from django.http import HttpResponse
from .models import enquiry,Reg


def std(request):
    return HttpResponse("<h1>Student App  </h1>")


def rn(request):
    object=enquiry.objects.all()
    param={'student':object,}

    print(object)
    print(param.items())
    return render(request,"roll.html",param)


def student(request):
    return render(request, 'std.html')


def gethome(request):
    return render(request, 'new1.html')


def signUp(request):
    name = request.GET.get('name', 'default')
    mobile = request.GET.get('mobilenumber', 'default')
    email = request.GET.get('email', 'default')
    emailm = request.GET.get('emailm', 'default')
    domain = request.GET.get('domain', 'default')
    course = request.GET.get('course', 'domain')
    qualification = request.GET.get('qualification', 'default')
    year = request.GET.get('year', 'default')
    city = request.GET.get('city', 'default')
    detail = request.GET.get('details', 'default')
    comment = request.GET.get('comment', 'default')
    print(name, mobile, email, emailm, domain, course, qualification, year, city, detail, comment, end=";")
    p = {'myName': name, 'mob': mobile, 'em': email, 'ml': emailm, 'dm': domain, 'course': course, 'q': qualification,
         'yr': year, 'cty': city, 'det': detail, 'com': comment}
    s = enquiry(name=name, mobilenumber=mobile, email=email, emailm=emailm, domain=domain, course=course,
                qualification=qualification, year=year, city=city)
    print(s)
    s.save();
    return render(request, 'represent.html', p)


def search(request):
    return render(request, "search.html")


def searchpage(request):
    dem = ''
    try:
        ar = request.GET.get('searchbox')
        print("Search   ==   ", ar)
        res = enquiry.objects.all()


        print("All Response = ",res)
        dem = enquiry.objects.get(namecadidateId=ar)
        qwe=enquiry.objects.filter(name_isnull=False)


        print(qwe +" is the result of filtering")
        print('name =',dem)

    except TypeError:
        print("Http code isnt integer")


    except:
        return HttpResponse('<h1>ID    doesnt exist.Try again</h1>')

    else:
        param = {'result': res, 'nm': dem, 'ar': ar}
        return render(request, 'serres.html', param)
