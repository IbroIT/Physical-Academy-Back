from django.urls import path
from .views import CorrespondenceFacultyDataAPIView

app_name = "correspondence_faculty"

urlpatterns = [
    path(
        "",
        CorrespondenceFacultyDataAPIView.as_view(),
        name="correspondence-faculty-data",
    ),
]
