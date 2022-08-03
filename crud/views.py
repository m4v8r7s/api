from django.shortcuts import render
from django.http import HttpResponse
from .models import full_Details

# Create your views here.

def index(request):
    return HttpResponse("HEllo")

def hello(request):
    return HttpResponse("Gelllo")


