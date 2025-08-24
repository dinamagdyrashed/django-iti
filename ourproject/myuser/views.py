from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Login(request):
    return HttpResponse('<h1>Hello from login</h1>')

def Logout(request):
    return HttpResponse('<h1>Hello from logout</h1>')

def Register(request):
    return HttpResponse('<h1>Hello from register</h1>')