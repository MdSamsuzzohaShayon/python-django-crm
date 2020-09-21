from django.shortcuts import render, redirect
# https://docs.djangoproject.com/en/3.1/intro/tutorial01/#write-your-first-view
from django.http import HttpResponse
# https://docs.djangoproject.com/en/3.1/ref/forms/models/#inlineformset-factory
# https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#inline-formsets
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
# https://docs.djangoproject.com/en/3.0/ref/contrib/messages/#using-messages-in-views-and-templates
from django.contrib import messages

# https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#module-django.contrib.auth.signals
# https://docs.djangoproject.com/en/3.1/topics/auth/default/#how-to-log-a-user-in
from django.contrib.auth import authenticate, login, logout
# https://docs.djangoproject.com/en/2.2/_modules/django/contrib/auth/decorators/
# https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.decorators.login_required
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter


# Create your views here.


# https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/
def registerPage (request):
    # https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#django.contrib.auth.models.User.is_authenticated
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)
                return redirect('login')
        context ={
            "form": form
        }
        return render(request, 'accounts/register.html', context)



def loginPage (request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if(request.method == 'POST'):
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request , user)
                return redirect('home')
            else:
                messages.info(request, "Username or password is incorrect")

        context ={}
        return render(request, 'accounts/login.html', context)



def logoutUser(request):
    logout(request)
    return redirect('login')



# https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.decorators.login_required
# https://docs.djangoproject.com/en/3.1/ref/request-response/
@login_required(login_url='login')
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




@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    # https://docs.python.org/3/tutorial/datastructures.html#dictionaries
    return render(request, 'accounts/products.html', {'products': products})







@login_required(login_url='login')
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()

    # https://django-filter.readthedocs.io/en/master/
    # https://pypi.org/project/django-filter/

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'customer' : customer,
        "orders" : orders,
        "order_count": order_count,
        "myFilter" : myFilter
    }
    return render(request, 'accounts/customer.html', context)







@login_required(login_url='login')
def createOrder(request, pk):
    # https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#inline-formsets
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet( queryset=Order.objects.none() ,instance = customer)
    # form = OrderForm(initial={'customer': customer})
#    3 BY DEFAULT IT'S GET REQUEST BUT WE ARE MAKING IT POST'
    if request.method == "POST":
        #print('Printing post: ', request.POST)
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {
        "formset" : formset
    }
    return render(request, "accounts/order_form.html", context)



@login_required(login_url='login')
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



@login_required(login_url='login')
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
