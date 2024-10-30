from ..views.users import (
    CustomerRegisterAPIView,
    CustomerListAPIView,
    CustomerLoginAPIView, 
    CustomerProfileAPIView,
    CustomerPasswordResetAPIView
)
from django.urls import path

urlpatterns = [
    path('api/customer/register/', CustomerRegisterAPIView.as_view(), name = 'api-customer-register'),
    path('api/customer/list/', CustomerListAPIView.as_view(), name = 'api-customer-list'),
    path('api/customer/login/',CustomerLoginAPIView.as_view(), name = 'api-customer-login'),
    path('api/customer/profile/', CustomerProfileAPIView.as_view(), name = 'api-customer-profile'),
    path('api/customer/password/reset/', CustomerPasswordResetAPIView.as_view(), name = 'api-customer-password-reset')
]
