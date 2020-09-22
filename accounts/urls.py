"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


urlpatterns = [
    # https://docs.djangoproject.com/en/3.1/ref/urls/
    # https://docs.djangoproject.com/en/3.1/topics/http/urls/
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
    # http://127.0.0.1:8000/products/
    path('products/', views.products, name="products"),
    # http://127.0.0.1:8000/customers/
    # https://docs.djangoproject.com/en/3.1/topics/http/urls/
    # https://docs.djangoproject.com/en/3.1/topics/http/urls/#reverse-resolution-of-urls
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('create_order/<str:pk>', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),
    path('about/', views.about),
]
