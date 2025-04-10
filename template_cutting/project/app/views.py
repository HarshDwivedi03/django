from django.shortcuts import render


def base(req):
    return render(req,'landingpage.html')
# Create your views here.
def about(req):
    return render(req,'about.html')
def home(req):
    return render(req,'home.html')
def contact(req):
    return render(req,'contact.html')
def services(req):
    return render(req,'service.html')
def registration(req):
    return render(req,'registration.html')
def login(req):
    return render(req,'login.html')
def register(request):
    name=request.POST.get('username')
    email=request.POST.get('email')
    detail=request.POST.get('detail')
    phone=request.POST.get('phone')
    dob=request.POST.get('dob')
    subcribe=request.POST.get('subcribe')
    gender=request.POST.get('gender')
    password=request.POST.get('password')
    cpassword=request.POST.get('password')
    pc=request.FILES.get('profile pic')
    r=request.FILES.get('resume')
    print(name,email,detail,phone,dob,subcribe,gender,password,cpassword,pc,r)