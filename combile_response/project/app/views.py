from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
def home(request):
    data=[{'name':'harsh','age':37,},{'name':'lovekhush','age':30,}]
    user={'name':'ankit','city':'bhopal'}
    return render(request,'home.html',{"key1":user,'key2':data})
def index(request):
    return render(request,'index.html')
def index(request):
    return redirect (request,'index.html')
def tc(request):
    return HttpResponse('<h1>hello<h1/>')
# def home(request):
#     return render(request,'index.html')
def js(request):
    data={'name':True,'age':False}
    return JsonResponse(data)

# Create your views here.
