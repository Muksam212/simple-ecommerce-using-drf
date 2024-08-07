from rest_framework import serializers
from .models import *


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    order_products = OrderItemSerializer(many = True)
    class Meta:
        model = Product
        fields = ("name","description","price","category","stock","updated_at", "order_products")
        depth = 1

class CategorySerializer(serializers.ModelSerializer):
    #nested serializers
    products = ProductSerializer(many = True)
    class Meta:
        model = Category
        fields = ("id","name", "slug", "description", "products")



class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many = True)
    class Meta:
        model = Order
        fields = "__all__"

