from django.shortcuts import render
from .models import countrymaster, statemaster
from django.http import HttpResponse,JsonResponse


# Create your views here.
def run1(request):
    countryname = countrymaster.objects.all()
    statename = statemaster.objects.all()
    print(countryname, statename)
    param = {'countryname': countryname, 'statename': statename}
    return render(request, 'run2.html', param)

def getstate(request):
    cid=request.GET.get('cid')
    countryname=countrymaster.objects.filter(cid=cid)
    print(countryname)
    return HttpResponse(countryname)

#def getcid(request):
