from django.http import HttpResponse
from django.shortcuts import render


def anytime(request):

    return render(request,"start.html")

def startextended(request):
    if request.method =="GET":
        selct = request.GET["select"]
        if selct == "password":
            return render(request,'loginpage.html')
        if selct == "Driving licence":
            return render(request,"next.html")
        if selct == "Average word/Play Scribble":
            return render(request,'average.html')
        if selct == "expression":
            return render(request,"expression.html")

def check(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass']
        string = password
        no = 0
        success = 0
        from string import punctuation, digits

        while True:

            count1 = 0
            count2 = 0
            for i in string:
                if i in digits:
                    count1 += 1
                if i in punctuation:
                    count2 += 1
            if len(string) >= 8:
                if count1 >= 4:
                    if count2 >= 4:
                        message = "Strong password,Your password fullfills every aspect "
                        success += 1

                    else:
                        no = 4 - count2
                        message = "more punctuatuions needed"
                else:
                    no = 4 - count1
                    message = "more numbers needed"

            else:
                no = 8 - len(string)
                message = "more Words needed"

            if no == 0:
                no = ""
            print(no, message)
            print(request.method)
            param = {'email': email, 'password': password, 'message': message, 'no': no, 'success': success}
            return render(request, "extended.html", param)


def login(request):
    return render(request, "loginpage.html")


def next(request):
    print(request.method)
    print("going to next.html")

    return render(request, "next.html")


def exnext(request):
    if request.method == "POST":
        myname = request.POST['name']
        Available_agent = int(request.POST['agent'])
        input_customer = request.POST['othername']

        from math import floor, ceil

        other_customers = []

        other_customers = input_customer.split(" ")

        other_customers.append(myname)
        other_customers.sort()
        print(other_customers)
        token_number = other_customers.index(myname) + 1

        print(token_number)

        roundn = ceil(token_number / Available_agent)
        print((roundn))

        if token_number == 1:
            a = 20


        else:
            a = roundn * 20
           
        param = {'a': a}

    return render(request, "extendednext.html", param)

