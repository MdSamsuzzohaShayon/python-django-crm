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
    path('', views.home),
    # http://127.0.0.1:8000/products/
    path('products/', views.products),
    # http://127.0.0.1:8000/customers/
    path('customer/', views.customer),
    path('about/', views.about),
]
