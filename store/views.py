from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from .models import (
						Product,
						Order,
						OrderItem,
)
import json
# Create your views here.


class Store(generic.ListView):
	template_name = "store/store.html"


	def get_context_data(self, *args, **kwargs):
		context = super(Store, self).get_context_data(*args, **kwargs)
		context["products"] = self.object_list["products"]
		context["items"] = self.object_list["items"] #--->Multiple context objects for rendering
		context["order"] =self.object_list["order"]
		context["cartItems"] = self.object_list["cartItems"]
		# context["products"] = context["object_list"] # parsing in built object_list to products for custom templating 
		return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		if request.user.is_authenticated:
			customer = request.user.customer #---> customer and user have OneToOne relationship
			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			items = order.orderitem_set.all()
			cartItems = order.get_cart_items
		else:
			items =[]
			order= { "get_cart_total":0, "get_cart_items":0}
			cartItems = order['get_cart_items']
			
		products = 	Product.objects.all()
		return { "items": items, "order":order, "products":products, "cartItems":cartItems}




class Cart(generic.ListView):
	template_name = "store/cart.html"
	# context_object_name = 'items'


	def get_context_data(self, *args, **kwargs):
		context = super(Cart, self).get_context_data(*args, **kwargs)
		context["items"] = self.object_list["items"] #--->Multiple context objects for rendering
		context["order"] =self.object_list["order"]
		context["cartItems"] = self.object_list["cartItems"]
		return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		if request.user.is_authenticated:
			customer = request.user.customer #---> customer and user have OneToOne relationship
			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			items = order.orderitem_set.all()
			cartItems = order.get_cart_items
		else:
			items =[]
			order= { "get_cart_total":0, "get_cart_items":0 }
			cartItems = order['get_cart_items']	
		return { "items": items, "order":order, "cartItems":cartItems}




class Checkout(Cart):
	template_name = "store/checkout.html"

	def get_context_data(self, *args, **kwargs):
		context = super(Checkout, self).get_context_data(*args, **kwargs)
		context["text"] = "this is the checkout"
		return context

# update item view
	
def updateitem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)