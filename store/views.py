from django.shortcuts import render
from django.views import generic
from .models import (
						Product,
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



class Cart(generic.TemplateView):
	template_name = "store/cart.html"

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context["text"] = "this is the cart"
		return context



class Checkout(generic.TemplateView):
	template_name = "store/checkout.html"

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context["text"] = "this is the checkout"
		return context
	
