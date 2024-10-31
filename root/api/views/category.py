from ..serializers.category import(
    CategorySerializer
)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ecommapp.models import Category

from .filters import CategoryFilter
from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import Q

class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = CategoryFilter
    model = Category

    #Implementation of search functionality using the Q module.
    def get_queryset(self):
        queryset = super().get_queryset()
        search_queryset = self.request.query_params.get("search", None)

        if search_queryset:
            queryset =  queryset.filter(
                Q(name__icontains = search_queryset) |
                Q(slug__icontains = search_queryset)
            )

        return queryset


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    model = Category
    lookup_field = "slug"