from django.db import models
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
from django.contrib.auth.models import User

# Create your models here.
# https://docs.djangoproject.com/en/3.1/intro/tutorial02/#creating-models
class Customer(models.Model):
    # https://docs.djangoproject.com/en/3.1/topics/db/examples/one_to_one/
    user  = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.CharField
    name = models.CharField(max_length=200, null=True)

    phone =  models.CharField(max_length=200, null=True)
    email =  models.CharField(max_length=200, null=True)
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#imagefield
    profile_pic = models.ImageField(default="default-pro-pic.jpg", null=True, blank=True)
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.DateTimeField
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


# https://docs.djangoproject.com/en/3.1/intro/tutorial02/#creating-models
class Tag(models.Model):
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.CharField
    name = models.CharField(max_length=200, null=True)

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
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    # https://docs.python.org/3.3/library/stdtypes.html?highlight=tuple#tuples
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    # https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/
    # https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/#many-to-one-relationships
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)
    def __str__(self):
        return self.product.name