from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Stud1 Application")

def addstud1(request):
    return HttpResponse("Student Registration")
