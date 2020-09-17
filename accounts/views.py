from django.shortcuts import render
# https://docs.djangoproject.com/en/3.1/intro/tutorial01/#write-your-first-view
from django.http import HttpResponse


# Create your views here.



# https://docs.djangoproject.com/en/3.1/ref/request-response/
def home(request):
    # https://docs.djangoproject.com/en/3.1/intro/tutorial03/#a-shortcut-render
    return render(request, 'accounts/dashboard.html')

def products(request):
    return render(request, 'accounts/products.html')

def customer(request):
    return render(request, 'accounts/customer.html')

def about(request):
    return HttpResponse('About page')
