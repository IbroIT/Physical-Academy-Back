from django.urls import path
from .views import (
    MilitaryFacultyTabsAPIView,
    MilitaryFacultyCardsAPIView,
    MilitaryFacultyHistoryAPIView,
)

app_name = "military_faculty"

urlpatterns = [
    path("tabs/", MilitaryFacultyTabsAPIView.as_view(), name="tabs"),
    path("cards/", MilitaryFacultyCardsAPIView.as_view(), name="cards"),
    path("history/", MilitaryFacultyHistoryAPIView.as_view(), name="history"),
]
