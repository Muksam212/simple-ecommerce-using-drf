from ..views.category import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView
)
from django.urls import path

urlpatterns = [
    path('api/category/list/', CategoryListCreateAPIView.as_view(), name = 'api-category-list'),
    path('api/category/retrieve/<slug:slug>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name = 'api-category-retrieve')
]
