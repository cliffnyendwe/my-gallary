from django.shortcuts import render
import datetime as dt
# Create your views here.
from django.http import HttpResponse

# create my views here

def welcome(request):
    return HttpResponse('Welcome to my Gallary')

def welcome(request):
    return render(request,'index.html')
            