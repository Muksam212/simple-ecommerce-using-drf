from ..serializers.users import (
    CustomerRegisterSerializer, CustomerListSerializer, CustomerLoginSerializer, CustomerProfileSerializer,
    CustomerPasswordResetSerializer
)
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView

from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from ecommapp.models import Customer
from users.models import User

from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }


class CustomerRegisterAPIView(CreateAPIView):
    serializer_class = CustomerRegisterSerializer

    def post(self, request, format = None):
        serializer = CustomerRegisterSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg":"success"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"error":"failed"}, status = status.HTTP_404_NOT_FOUND)



class CustomerListAPIView(ListAPIView):
    serializer_class = CustomerListSerializer
    queryset = Customer.objects.all()
    model = Customer


class CustomerLoginAPIView(CreateAPIView):
    serializer_class = CustomerLoginSerializer

    def post(self, request, format = None):
        serializer = CustomerLoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            username = serializer.data.get("username")
            password = serializer.data.get("password")

            usr = authenticate(username = username, password = password)
            if usr is not None:
                token = get_tokens_for_user(usr)
                return Response(token, status = status.HTTP_201_CREATED)
            else:
                return Response({"details":"Username or Password Incorrect"}, status = status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class CustomerProfileAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = CustomerProfileSerializer(user)
        return Response(serializer.data)
    

class CustomerPasswordResetAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomerPasswordResetSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        
        # Customize the response with a success message
        return Response({
            "message": "Password reset successfully!"
        }, status=status.HTTP_200_OK)