from django.shortcuts import render
from django.http import HttpResponse
from app1.models import User


def welcome(request):
    return render(request, 'app1/welcome.html')


def success(request):
    username = request.POST['userName']
    userpassword = request.POST['userPassword']
    a = User(userName=username, userPassword=userpassword)
    a.save()
    users = User.objects.latest('id')
    dict1 = {
        "users": users
        }

    return render(request, 'app1/success.html', dict1)
