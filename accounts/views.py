from django.shortcuts import render
# https://docs.djangoproject.com/en/3.1/intro/tutorial01/#write-your-first-view
from django.http import HttpResponse


# Create your views here.



# https://docs.djangoproject.com/en/3.1/ref/request-response/
def home(request):
    return HttpResponse("Home page")

def products(request):
    return HttpResponse('Products page')

def customers(request):
    return HttpResponse('Customers page')
