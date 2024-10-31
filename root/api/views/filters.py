import django_filters

from ecommapp.models import *

class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="iexact")
    slug = django_filters.CharFilter(field_name="slug", lookup_expr="iexact")
    class Meta:
        model = Category
        fields = ("name", "slug")