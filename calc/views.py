from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request,'home.html',{'name':'Rohit'})


def result(request):
    a = int(request.POST["num1"])
    b = int(request.POST["num2"])
    ans = a+b
    return render(request,'result.html',{'ans':ans})