from django.shortcuts import render,redirect
from django.http import HttpResponse
def home(request):
    name,city='harsh','bhopal'
    return redirect(f'/index/?name={name}&city={city}')
def index(request):
    print(request.method)
    print(request.GET)
    x=request.GET.get('name')
    y=request.GET.get('city')
    print(x,y)

# Create your views here.
