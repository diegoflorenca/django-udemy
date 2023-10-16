from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(requsest):
    return HttpResponse('This works!')


def february(request):
    return HttpResponse('This is the February challenge I\'ve made myself')
