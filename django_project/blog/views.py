from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1>Blog Home</h>')

def about(request):
    return HttpResponse('<h1>About</h1>')
