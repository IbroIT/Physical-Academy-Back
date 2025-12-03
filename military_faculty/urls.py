from django.urls import path
from .views import MilitaryFacultyDataAPIView

app_name = "military_faculty"

urlpatterns = [
    path("", MilitaryFacultyDataAPIView.as_view(), name="military-faculty-data"),
]
