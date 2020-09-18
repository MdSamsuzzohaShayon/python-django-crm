from django.shortcuts import render
# https://docs.djangoproject.com/en/3.1/intro/tutorial01/#write-your-first-view
from django.http import HttpResponse
from .models import *


# Create your views here.



# https://docs.djangoproject.com/en/3.1/ref/request-response/
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers =customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    context = {
        'orders': orders,
        'custemers': customers,
        "total_orders" : total_orders,
        "delivered": delivered,
        "total_customers": total_customers,
        'pending': pending
    }


    # https://docs.djangoproject.com/en/3.1/intro/tutorial03/#a-shortcut-render
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    # https://docs.python.org/3/tutorial/datastructures.html#dictionaries
    return render(request, 'accounts/products.html', {'products': products})

def customer(request):
    return render(request, 'accounts/customer.html')

def about(request):
    return HttpResponse('About page')
