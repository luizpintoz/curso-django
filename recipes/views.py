from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home.html')

def popular_foods(request):
    return HttpResponse('Food')
