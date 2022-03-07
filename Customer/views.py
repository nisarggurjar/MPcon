import json
import requests
from django.shortcuts import redirect, render
from django.http import HttpResponse
from Customer.models import UserInfo
from Management.views import CommonData
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# def Home(request):
#     return HttpResponse("<h2>Hello World</h2><p>How are you?</p>")

def Home(request):
    data = { 
        "title":"Fashion Hub"
    }
    data.update(CommonData())
    return render(request, 'index.html',data)


def SignUp(request):
    if request.user.is_authenticated:
        return redirect('home')
    errorUn = False
    errorPWD = False
    errorPin = False
    if request.method == "POST":
        data = request.POST
        un = data['un']
        e = data['email']
        pwd1 = data['Password']
        pwd2 = data['Password2']
        mob = data['mob']
        pin = data['pin']


        ## Pin Validation
        api = "https://api.postalpincode.in/pincode/{}".format(pin)
        response = requests.get(api)
        response_text = response.text
        response_json = json.loads(response_text)
        status = response_json[0]['Status']

        ##
        check = User.objects.filter(username = un).first()
        if pwd1 != pwd2:
            errorPWD = True
        elif check:
            errorUn = True
        elif status == "Error":
            errorPin = True
        else:
            user = User.objects.create_user(username = un, email = e, password = pwd1)
            UserInfo.objects.create(user = user, mobile = mob, pincode = pin)
            return redirect("home")
    data = { 
        "title":"Fashion Hub",
        "errorUn":errorUn,
        "errorPWD":errorPWD,
        "errorPin":errorPin
    }
    data.update(CommonData())
    return render(request, 'register.html', data)

def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    err = False
    if request.method == "POST":
        un = request.POST['un']
        pwd = request.POST['pwd']
        auth = authenticate(username = un, password = pwd)
        if auth:
            login(request, auth)
            return redirect("home")
        else:
            err = True
    data = {
        "title":"Login @ Fashion Hub",
        "err":err
    }
    data.update(CommonData())
    return render(request, 'login.html', data)

def LogOut(request):
    logout(request)
    return redirect("home")
