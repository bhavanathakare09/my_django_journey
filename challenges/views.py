from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("This is January")

def february(request):
    return HttpResponse("This is February")

def march(request):
    return HttpResponse("This is March")

def april(request):
    return HttpResponse("This is April")

def may(request):
    return HttpResponse("This is May")

def june(request):
    return HttpResponse("This is June")

def july(request):
    return HttpResponse("This is July")

def august(request):  
    return HttpResponse("This is August")

def september(request):
    return HttpResponse("This is September")  
  
def october(request):
    return HttpResponse("This is October")

def november(request):
    return HttpResponse("This is November")

def december(request):  
    return HttpResponse("This is December")


