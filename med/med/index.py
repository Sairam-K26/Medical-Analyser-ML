from django.http import HttpResponse
from django.shortcuts import render

def webpage(request):
    return render(request,'index.html')

def webpage2(request):
    return render(request,'stress.html')
