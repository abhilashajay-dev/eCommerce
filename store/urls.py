from django.urls import path
from .views import (
					Store,
					Cart,
					Checkout,

)

urlpatterns = [
path("", Store.as_view(), name='store'),
path("cart/", Cart.as_view(), name='cart'),
path("checkout/", Checkout.as_view(), name='checkout'),

]