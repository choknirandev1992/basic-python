from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, EMS

# Create your views here.

def Home(request):
    #return HttpResponse('<h1>Hello world</h1>')
    allmobile = Product.objects.all()
    #context = {'phonelist': ['I Phone X','Heuwei','samsung','oppo']}
    context = { 'phonelist': allmobile ,'title': 'Home'}
    return render(request, 'mobile/home.html', context)

def EMStracking(request):
    #return HttpResponse('<h1>Hello world</h1>')
    allems = EMS.objects.all()
    #context = {'phonelist': ['I Phone X','Heuwei','samsung','oppo']}
    context = { 'emslist': allems ,'title': 'EMS'}
    return render(request, 'mobile/ems.html', context)

def About(request):
    #return HttpResponse('<h1>About US</h1>')
    return render(request,'mobile/about.html')  


   