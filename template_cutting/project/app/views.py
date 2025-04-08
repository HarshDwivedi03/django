from django.shortcuts import render


def base(req):
    return render(req,'landingpage.html')
# Create your views here.
def about(req):
    return render(req,'about.html')
def contact(req):
    return render(req,'contact.html')
def services(req):
    return render(req,'service.html')
def registration(req):
    return render(req,'registration.html')
def login(req):
    return render(req,'login.html')