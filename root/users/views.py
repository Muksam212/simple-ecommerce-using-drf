from django.shortcuts import render

from .serializers import *
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .renderers import UserRenderers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }

class UserRegisterViewSet(ModelViewSet):
    serializer_class = UserRegisterSerializer
    model = User
    queryset = User.objects.all()


class UserLoginViewSet(ModelViewSet):
    serializer_class = UserLoginSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception = True):
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")

            usr = authenticate(username = username, password = password)

            if usr is not None:
                token = get_tokens_for_user(usr)
                return Response(token, status=status.HTTP_200_OK)
            else:
                return Response({
                    "details":"Username or Password is not valid"
                }, status = status.HTTP_404_NOT_FOUND)
            
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

class UserPasswordChangeViewSet(ModelViewSet):
    serializer_class = UserPasswordResetSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = request.user
        print(user,"===============")
        if not user.check_password(serializer.validated_data["old_password"]):
            return Response({"old_password":"Old password is not correct"}, status = status.HTTP_400_BAD_REQUEST)
        user.set_password(serializer.validated_data["password"])
        user.save()
        return Response({"status":"password set"}, status = status.HTTP_200_OK)
