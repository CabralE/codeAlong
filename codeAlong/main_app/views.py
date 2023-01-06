from django.shortcuts import render, redirect

# Testing Standard HTTP Res... this can be deleted for Production
from django.http import HttpResponse

# connecting Models to Views
from .models import sample,Leetcode

# 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def practice(request):
    leetcodes = Leetcode.objects.all()
    return render(request, 'leetcodes/index.html', {'leetcodes': leetcodes})

def practice_details(request, leetcode_id):
    leetcode = Leetcode.objects.get(id=leetcode_id)
    return render(request, 'leetcodes/detail.html', {'leetcode': leetcode})

def study(request):
    return render(request, 'study.html')

# def login(request):
#     return render(request, 'login.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('about')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


    

