from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantitiy = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    
class ShippingAddress(models.Model):
    
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address