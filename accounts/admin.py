from django.contrib import admin

# Register your models here.

#from .models import Customer
from .models import *

# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)