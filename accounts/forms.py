# https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/
from django.forms import ModelForm

from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        # FOR ALL INDIVIDUAL ITEMS USE THE VARIABLE FROM ORDER MODEL
        # fields = ["customer", 'product']