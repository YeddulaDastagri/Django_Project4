from django.shortcuts import render 
from django.http import HttpResponse 

# Create your views here.

def veg(request):
    return HttpResponse('ramu is a vegetarian')