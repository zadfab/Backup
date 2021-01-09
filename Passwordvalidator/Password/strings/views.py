from django.shortcuts import render
from math import ceil
from string import punctuation


# Create your views here.

def average(request):
    print(request.method)
    return render(request, "average.html")


def averagestring(request):
    if request.method == "POST":
        string = request.POST["string"]
        improvedstring = ""
        for i in string:
            if i == " ":
                improvedstring = improvedstring + i
            elif i not in punctuation:
                improvedstring = improvedstring + i
        nospace = improvedstring.replace(" ", "")

        print("improved string is ->", nospace)
        array = improvedstring.split(" ")
        print(array)
        result = ceil(len(nospace) / len(array))
        param = {'result': result}
    return render(request, "Extendedaverage.html", param)


def scribble(request):
    if request.method == "POST":

        user_string = request.POST["string"]
        print(user_string)
        points = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}


        dict ={}
        improved_user_string = user_string.split(" ")
        words =str((len(improved_user_string) - 10 ))
        print(words)
        if len(improved_user_string)  <= 10 :
            for i in improved_user_string:
                som = 0
                for j in i:
                    som = som + points[j]

                    dict.update({i:som})


            def getmax(read):
                v=list(read.values())
                k=list(read.keys())
                print(v)
                print(k)

                return k[v.index(max(v))]
            result = getmax(dict)
        else:
            result = str(words) +"  less word"


        print(type(result))

        param = {'res':result}
        return render(request,"extendedcribble.html",param)

def expressionextended(request):

    lower_bound = request.GET['']
    upper_bound = request.GET['']
    multiply = request.GET['']

    sum = 0

    for i in range(lower_bound,upper_bound+1):
        results =("{0}{1}".format(i,multiply))
        result = eval(results)
        sum = sum + result
    param = {'res':sum,'results':results}
    return render(request,'expressionextended.html',param)