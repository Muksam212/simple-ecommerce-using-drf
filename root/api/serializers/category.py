from rest_framework import serializers
from ecommapp.models import Category

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "description")