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
from django.contrib import admin
from django.urls import path, include

# SETTING STATIC FILES URLS PATTERN
# Helper function to return a URL pattern for serving files in debug mode:
# https://docs.djangoproject.com/en/1.8/ref/urls/#static
from django.conf.urls.static import static
# In your Django apps, use settings by importing the object django.conf.settings.
# https://docs.djangoproject.com/en/3.1/topics/settings/#using-settings-in-python-code
from django.conf import settings
from pyatspi import document

urlpatterns = [
    # https://docs.djangoproject.com/en/3.1/ref/urls/
    # https://docs.djangoproject.com/en/3.1/topics/http/urls/
    path('admin/', admin.site.urls),
    path('', include('accounts.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# check image url http://localhost:8000/img/mbappe.jpg
