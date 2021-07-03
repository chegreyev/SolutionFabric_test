from django.urls import path

from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="SolutionFabric__test",
      default_version='v1.2.3',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="chegreyev@gmail.com"),
      license=openapi.License(name="MY License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


swagger_patterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-swagger-ui')
]
