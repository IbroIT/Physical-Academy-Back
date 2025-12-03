from django.urls import path
from .views import CoachingFacultyDataAPIView

app_name = "coaching_faculty"

urlpatterns = [
    path("", CoachingFacultyDataAPIView.as_view(), name="coaching-faculty-data"),
]
