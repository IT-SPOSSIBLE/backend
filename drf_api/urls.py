from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from django.conf import settings
from django.conf.urls.static import static

# Define Swagger schema view
schema_view = get_schema_view(
   openapi.Info(
      title="My API",
      default_version='v1',
      description="Detailed API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@myapi.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('api.urls')),
    path('categories/', include('category.urls')),
    path('products/', include('product.urls')),
    path('messages/', include('message.urls')),
    path('conversations/', include('conversation.urls')),
    path('images/', include('motocycleImage.urls')),
   
    # Swagger UI documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    
    # ReDoc UI documentation (optional)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)