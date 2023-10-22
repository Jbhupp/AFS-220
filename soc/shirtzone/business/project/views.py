from django.shortcuts import render
from .views import *


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contactus(request):
    return render(request, 'contactus.html')

def gallery(request):
    return render(request, 'gallery.html')