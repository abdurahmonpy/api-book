from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.views.static import serve
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', include('books.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # OpenAPI 3 Schema & Swagger UI / Redoc Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui-alias'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Bosh sahifa va /api/ ni avtomatik Swagger dokumentatsiyasiga yo'naltirish
    path('', RedirectView.as_view(url='api/docs/', permanent=False)),
    path('api/', RedirectView.as_view(url='docs/', permanent=False)),

    # Media fayllarni (rasm va PDF) Railway / ishlab chiqarishda ham tarqatish
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
