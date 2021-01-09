from django.shortcuts import render,get_object_or_404
from .models import form
from django.http import HttpResponse

# Create your views here.

def start(request):
    return render(request,'start.html',{})

def submit(request):
    if request.method=='POST':
        name=request.POST['name']
        rollnumber=request.POST['rollnumber']
        address=request.POST['address']
        id=form.objects.all().order_by('-rollnumber').reverse()
        param={'name':name,'rollnumber':rollnumber,'address':address,'id':id}
        print(id)
        try:
            if len(name)>3 :
                student=form(name=name,rollnumber=rollnumber,address=address)
                student.save()
            else:
                HttpResponse('name Should be more than 3 character')
        except:
            HttpResponse("Rollnumber is already exists")




        return render(request,'results.html',param)

def search(request):
    if request.method=='POST':
        #rollnumber=request.POST['searchbox']
        lik=request.POST['searchboxlike']
       # result=form.objects.get(rollnumber=rollnumber)
       # print(result)

        fil=form.objects.filter(name__icontains=lik)
        print('-----____----_____---____----__')
        print('filtered data',fil)
        param={'filter':fil}

        return render(request,'extendresult.html',param)




def searchbox(request):
    if request.method=="POST":
        searchbox=request.POST['searchbox']
        print(searchbox)
        id=form.objects.get(rollnumber=searchbox)
        print(id)
        param={'id':id}
        return render(request,'checkbox.html',param)
