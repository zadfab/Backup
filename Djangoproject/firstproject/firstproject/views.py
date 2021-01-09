from django.shortcuts import render
from django.http import HttpResponse

#from firstproject.student.models import enquiry


def login(request):
    return HttpResponse("<h2>Hello login page<h2>")


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
  #  s=enquiry(name=name,mobile=mobile,email=email,mail=emailm,domain=domain,course=course,qualification=qualification,year=year,city=city)
   # s.save();
    return render(request, 'represent.html', p) ;

