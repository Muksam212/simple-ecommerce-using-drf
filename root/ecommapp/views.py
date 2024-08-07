from django.shortcuts import render

from .serializers import *
from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    model = Category
    queryset = Category.objects.all()

class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    model = Product


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    model = Order

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(user = user)
    

class OrderItemViewSet(ModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    model = OrderItem
    queryset = OrderItem.objects.all()