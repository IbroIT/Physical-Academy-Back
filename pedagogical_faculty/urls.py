from django.urls import path
from .views import PedagogicalFacultyDataAPIView

app_name = "pedagogical_faculty"

urlpatterns = [
    path("", PedagogicalFacultyDataAPIView.as_view(), name="pedagogical-faculty-data"),
]
