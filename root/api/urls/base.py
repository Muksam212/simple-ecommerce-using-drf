from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .users import urlpatterns as users_urlpatterns
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title="Ecommerce",
        default_version="v1",
        description="API Swagger",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@asparksys.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = (
    [
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
    ]
    + users_urlpatterns
)