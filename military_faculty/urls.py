from django.urls import path
from .views import (
    MilitaryFacultyAPIRootView,
    MilitaryFacultyTabsAPIView,
    MilitaryFacultyCardsAPIView,
    MilitaryFacultyHistoryAPIView,
)

app_name = "military_faculty"

urlpatterns = [
    path("", MilitaryFacultyAPIRootView.as_view(), name="api-root"),
    path("tabs/", MilitaryFacultyTabsAPIView.as_view(), name="tabs"),
    path("cards/", MilitaryFacultyCardsAPIView.as_view(), name="cards"),
    path("history/", MilitaryFacultyHistoryAPIView.as_view(), name="history"),
]
