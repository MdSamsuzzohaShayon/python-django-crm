from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/3.1/intro/tutorial02/#creating-models
class Customer(models.Model):
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.CharField
    name = models.CharField(max_length=200, null=True)
    phone =  models.CharField(max_length=200, null=True)
    email =  models.CharField(max_length=200, null=True)
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.DateTimeField
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product (models.Model):
    # https://docs.python.org/3.3/library/stdtypes.html?highlight=tuple#tuples
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length=200, null=True)
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.FloatField
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Order(models.Model):
    # https://docs.python.org/3.3/library/stdtypes.html?highlight=tuple#tuples
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    #customer =
    #product =
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)