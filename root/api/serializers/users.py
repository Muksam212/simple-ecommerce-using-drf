from django.db import transaction
from rest_framework import serializers
from users.models import User
from ecommapp.models import Customer

class CustomerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    confirm_password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ("username", "email", "password", "confirm_password", "user_image")
        extra_kwargs = {
            "confirm_password":{"write_only":True}
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"error":"Password didn't match"})
        return attrs
    
    @transaction.atomic
    def create(self, validated_data):
        validated_data.pop("confirm_password", None)

        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            user_image = validated_data.get("user_image", None)
        )
        #set the password
        user.set_password(validated_data["password"])
        user.save()

        #Instance
        Customer.objects.create(user = user)
        return user
    

class CustomerListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    username = serializers.CharField(source = "user.username")
    email = serializers.CharField(source = "user.email")
    class Meta:
        model = User
        fields = ("id", "username", "email")


class CustomerLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ("username", "password")


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class CustomerPasswordResetSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["old_password", "password", "confirm_password"]

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"error": "The Password confirmation does not match"}
            )

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
