from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hi I am Django Server")

def success_page(request):
    return HttpResponse("<h1>Hi Django</h2>")