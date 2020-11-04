from django.shortcuts import render
from django.views import generic
from .models import (
						Product,
						Order,
						OrderItem,
)
# Create your views here.


class Store(generic.ListView):
	template_name = "store/store.html"
	queryset = Product.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context["text"] = "this is the store"
		context["products"] = context["object_list"] # parsing in built object_list to products for custom templating 
		return context



class Cart(generic.ListView):
	template_name = "store/cart.html"
	# context_object_name = 'items'


	def get_context_data(self, *args, **kwargs):
		context = super(Cart, self).get_context_data(*args, **kwargs)
		context["items"] = self.object_list["items"] #--->Multiple context objects for rendering
		context["order"] =self.object_list["order"]
		return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		if request.user.is_authenticated:
			customer = request.user.customer #---> customer and user have OneToOne relationship
			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			items = order.orderitem_set.all()
		else:
			items =[]
			order= { "get_cart_total":0, "get_cart_items":0 }	
		return { "items": items, "order":order}




class Checkout(Cart):
	template_name = "store/checkout.html"

	def get_context_data(self, *args, **kwargs):
		context = super(Checkout, self).get_context_data(*args, **kwargs)
		context["text"] = "this is the checkout"
		return context
	
