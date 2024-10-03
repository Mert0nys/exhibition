from django.urls import path, include
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from cats.views import KittenViewSet, BreedViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Kitten Exhibition API",
      default_version='v1',
      description="API for managing kitten exhibitions",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@kitten.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = DefaultRouter()
router.register(r'kittens', KittenViewSet)
router.register(r'breeds', BreedViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('admin/', admin.site.urls),
   path('api/', include('cats.urls')),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]

