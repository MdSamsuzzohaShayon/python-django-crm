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
from django.contrib.auth.models import Group

from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter

from .decorators import unauthenticated_user, allowed_users, admin_only


# Create your views here.


# ACTUALLY IN UNAUTHENTICATED USER FUNCTION TAKING THIS REGISTER PAGE FUNCTION AS PARAMETER
# https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/
@unauthenticated_user
def registerPage (request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name="customer")
            user.groups.add(group)
            # CREATE USE AND CUSTOMER TOGETHER
            Customer.objects.create(
                user= user
            )
            messages.success(request, "Account was created for " + username)
            return redirect('login')
    context ={
        "form": form
    }
    return render(request, 'accounts/register.html', context)



@unauthenticated_user
def loginPage (request):
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



# ALLOWED USERS FUNCTION  WILL WORK INSIDE LOGIN REQUIRED FUNCTION
# https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.decorators.login_required
# https://docs.djangoproject.com/en/3.1/ref/request-response/
@login_required(login_url='login')
@admin_only
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
@allowed_users(allowed_roles=["customer"])
def userPage(request):
    print("userpage")
    orders = request.user.customer.order_set.all()
    print("orders ", orders)
    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()
    context = {
        "orders":orders,
        "total_orders": total_orders,
        "delivered": delivered,
        "pending": pending
    }
    return render(request, 'accounts/user.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=["customer"])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context ={
        "form": form
    }
    return render(request, 'accounts/account_settings.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=["admin"])
def products(request):
    products = Product.objects.all()
    # https://docs.python.org/3/tutorial/datastructures.html#dictionaries
    return render(request, 'accounts/products.html', {'products': products})







@login_required(login_url='login')
@allowed_users(allowed_roles=["admin"])
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
@allowed_users(allowed_roles=["admin"])
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
@allowed_users(allowed_roles=["admin"])
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
@allowed_users(allowed_roles=["admin"])
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
