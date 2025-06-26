from django.shortcuts import render 
from django.http import HttpResponse


def index(request):
    stats = {
        'users': 1234,
        'revenue': 9876,
        'errors': 3,
        'session': 6
    }
    return render(request, 'main/index.html', stats)

def home(request):
    return HttpResponse("This is my home page")