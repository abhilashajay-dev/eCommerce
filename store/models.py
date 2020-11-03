from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()


# Customer Model
class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	name = models.CharField(null=True, max_length=100)
	email = models.EmailField(max_length=200, null=True)


	def __str__(self):
		return self.name



# Product Model

class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False, null=True, blank=True)


	def __str__(self):
		return self.name 		


# Order Model

#  Cart 
class Order(models.Model): 
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, null=True, blank=True)
	transaction_id = models.CharField(max_length=200, null=True)

	def __str__(self):
		return int(self.id)


# Cart item
class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added  = models.DateTimeField(auto_now_add=True)


# Shipping Model

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address















