from django.shortcuts import render

from .models import leetcodes

# Create your views here.
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def practice(request):
    return render(request, 'leetcodes/index.html', {'leetcodes': leetcodes})

def study(request):
    return render(request, 'study.html')

def login(request):
    return render(request, 'login.html')

    

