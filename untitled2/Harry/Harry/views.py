from django.http import HttpResponse
from django.shortcuts import render


def pun1(request):
    return render(request, 'index.html')


def pun(request):
    bx = request.GET.get('box', 'default')
    check1 = request.GET.get('ck', 'off')
    check2 = request.GET.get('ck1', 'off')
    check3 = request.GET.get('ck2', 'off')
    check4 = request.GET.get('ck3', 'off')

    punctuation = ",.;':[]{}-_=+ /*-.^%$#@!~`"
    result = ""
    texti = ""
    if check1 == 'on':
        for i in bx:
            if i not in punctuation:
                result = result + i
        par = {'tx': bx, 'res': result}
        texti = result

    if check2 == 'on':
        result = texti.upper()
        par = {'res': result}
        texti = result

    if check3 == 'on':
        res = result.__len__()

        par = {'res': res}

    if check4 == 'on':

        for index, i in enumerate(texti):
            if not texti[index] == " " and texti[index + 1] == " ":
                result = result + i
        par = {'res': result}

    return render(request, 'home.html', par)


def pop1(request):
    return HttpResponse(''' <a href=''></a>''')


def pop2(request):
    return HttpResponse(''' This is Facebook Website Click<a href='https://www.facebook.com/'>Here</a>to open<br>
    CLick <a href="http://127.0.0.1:8010/">Here</a> to go home''')


def pop3(request):
    return HttpResponse('''This is Twitter Website Click <a href='https://twitter.com/home'>Here</a><br>
    CLick <a href="http://127.0.0.1:8010/facebook">Here</a> to go back''')


def pop4(request):
    return HttpResponse(''' This is Youtube Website Click <a href='https://www.youtube.com/'>Here</a><br>
    CLick <a href="http://127.0.0.1:8010/twitter">Here</a> to go back''')
