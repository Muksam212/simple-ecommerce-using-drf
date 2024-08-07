from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'category', views.CategoryViewSet, basename = "category-viewset")
router.register(r'product', views.ProductViewSet, basename = 'product-viewset')
router.register(r'order', views.OrderViewSet, basename = 'order-viewset')
router.register(r'items', views.OrderItemViewSet, basename = 'order-item-viewset')

urlpatterns = [
    path('', include(router.urls))
]
