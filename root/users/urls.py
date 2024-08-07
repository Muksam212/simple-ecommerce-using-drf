from django.urls import path, include
from .import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users/register', views.UserRegisterViewSet, basename = 'user-register')
router.register(r'users/login', views.UserLoginViewSet, basename='user-login')
router.register(r'user/password/reset', views.UserPasswordChangeViewSet, basename='user-reset')

urlpatterns = [
    path('', include(router.urls))
]
