from django.urls import path
from .views import (
    CoachingFacultyTabsAPIView,
    CoachingFacultyCardsAPIView,
    CoachingFacultyHistoryAPIView,
)

app_name = "coaching_faculty"

urlpatterns = [
    path("tabs/", CoachingFacultyTabsAPIView.as_view(), name="tabs"),
    path("cards/", CoachingFacultyCardsAPIView.as_view(), name="cards"),
    path("history/", CoachingFacultyHistoryAPIView.as_view(), name="history"),
]
