from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'micro/base.html')

def home(request):
    return render(request,'micro/home.html') 

def plan(request):
    return render(request,'micro/plans.html')      

def blog(request):
    return render(request,'micro/blog.html') 

def pay(request):
    return render(request,'micro/payment.html')   


def error(request):
    return render(request,'micro/error.html')  

def support(request):
    return render(request,'micro/support.html')

