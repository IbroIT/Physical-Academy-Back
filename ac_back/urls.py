from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

# drf-spectacular imports
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

# drf-spectacular schema/views
urlpatterns = [
    path("admin/", admin.site.urls),
    # API URLs
    path('api/student-clubs/', include('student_clubs.urls')),
    path('api/leadership-structure/', include('leadership_structure.urls')),
    path('api/admission/', include('admission.urls')),

    # # Swagger / Redoc documentation
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$',
    #         schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
