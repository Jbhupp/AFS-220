from django.shortcuts import render
from .views import *


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def random(request):
    return render(request, 'random.html')