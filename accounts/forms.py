# https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/

from django.forms import ModelForm
# https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/
from django.contrib.auth.forms import UserCreationForm
from django import forms
# https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#user-model
from django.contrib.auth.models import User

from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        # FOR ALL INDIVIDUAL ITEMS USE THE VARIABLE FROM ORDER MODEL
        # fields = ["customer", 'product']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']