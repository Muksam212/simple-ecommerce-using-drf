from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register([
    Customer,
    Category,
    ProductImage,
    Product,
    Order,
    OrderItem,
    Review,
    WishList,
    ShippingAddress,
    BillingAddress
])