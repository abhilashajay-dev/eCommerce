from django.urls import path
from .views import (
					Store,
					Cart,
					Checkout,
					updateitem,

)

urlpatterns = [
path("", Store.as_view(), name='store'),
path("cart/", Cart.as_view(), name='cart'),
path("checkout/", Checkout.as_view(), name='checkout'),
path("update_item/", updateitem, name='update_item'),

]