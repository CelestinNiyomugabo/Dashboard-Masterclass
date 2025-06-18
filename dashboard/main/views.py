from django.shortcuts import render 
from django.http import HttpResponse


def index(request):
    return HttpResponse(56)

def home(request):
    return HttpResponse("This is my home page")