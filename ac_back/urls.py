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
    path("api/student-clubs/", include("student_clubs.urls")),
    path("api/leadership-structure/", include("leadership_structure.urls")),
    path("api/admission/", include("admission.urls")),
    path("api/science/", include("science.urls")),
    # OpenAPI / Swagger / Redoc via drf-spectacular
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
