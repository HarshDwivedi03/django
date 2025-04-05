from django.shortcuts import render
from django.http import JsonResponse
def app4(request):
    data={'name':'harsh','age':26,'qualifi':'btech'}
    return JsonResponse(data)
     

# Create your views here.
