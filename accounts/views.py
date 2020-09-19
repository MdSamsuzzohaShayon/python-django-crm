from django.shortcuts import render, redirect
# https://docs.djangoproject.com/en/3.1/intro/tutorial01/#write-your-first-view
from django.http import HttpResponse
from .models import *
from .forms import OrderForm



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







def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {
        'customer' : customer,
        "orders" : orders,
        "order_count": order_count
    }
    return render(request, 'accounts/customer.html', context)








def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer': customer})
#    3 BY DEFAULT IT'S GET REQUEST BUT WE ARE MAKING IT POST'
    if request.method == "POST":
        #print('Printing post: ', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form" : form
    }
    return render(request, "accounts/order_form.html", context)




def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        #print('Printing post: ', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request, "accounts/order_form.html", context)



def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')


    context = {
        "item" : order
    }
    return render(request, "accounts/delete.html", context)







def about(request):
    return HttpResponse('About page')
