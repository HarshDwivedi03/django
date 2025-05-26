from django.shortcuts import render
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from .serializers import *

    # Create your views here.
def student_list(request):
    stu = Student.objects.all()
    serializer=StudentSerialzers(stu, many=True) #
    print("Serializer= ",serializer)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)

    #print("Json_data = ",json_data)
    return HttpResponse(json_data,content_type='application/json')

    #when we send json data from views then contet type must be a "application/json"

    #return JsonResponse(serializer.data, safe=False) #

    #first argument of JsonResponse should be a dict, otherwise set safe=False
def student_detail(req,pk):
    user=Student.objects.get(pk=pk)
    serializer = StudentSerialzers(user)
    print("Serializer= ",serializer)
    print(serializer.data)

    #json_data = JSONRenderer().render(serializer.data)

    #print("Json_data = ", json_data)

    

    #return HttpResponse(json_data,content_type='application/json')

    #when we send json data from views then contet type must be a "application/json"

    return JsonResponse(serializer.data, safe=False)

    #first argument of JsonResponse should be a dict, otherwise set safe=False