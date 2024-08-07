from rest_framework import serializers
from users.models import User
from ecommapp.serializers import *

class UserRegisterSerializer(serializers.ModelSerializer):
    users_order = OrderSerializer(many = True)
    confirm_password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ("id","username", "email", "password", "confirm_password", "users_order")
        extra_kwargs = {
            "password":{"write_only":True}
        }

    def validated(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Password didn't match")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop("confirm_password", None)
        return User.objects.create_user(**validated_data)
    

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ("username", "password")



class UserPasswordResetSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = True)
    old_password = serializers.CharField(write_only = True, required = True)
    confirm_password = serializers.CharField(write_only = True, required = True)
    class Meta:
        model = User
        fields = ("password", "old_password", "confirm_password")

    
    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Password didn't match")
        return attrs
    

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError({"error": "Old password is not correct"})
        return value
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
    

class UserListSerializer(serializers.ModelSerializer):
    users_order = OrderSerializer(many = True)
    class Meta:
        model = User
        fields = ("id", "username", "users_order")