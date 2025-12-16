from django.urls import path
from .views import (
    CorrespondenceFacultyAPIRootView,
    CorrespondenceFacultyTabsAPIView,
    CorrespondenceFacultyCardsAPIView,
    CorrespondenceFacultyHistoryAPIView,
    CorrespondenceFacultyAboutAPIView,
)

app_name = "correspondence_faculty"

urlpatterns = [
    path("", CorrespondenceFacultyAPIRootView.as_view(), name="api-root"),
    path("tabs/", CorrespondenceFacultyTabsAPIView.as_view(), name="tabs"),
    path("cards/", CorrespondenceFacultyCardsAPIView.as_view(), name="cards"),
    path("history/", CorrespondenceFacultyHistoryAPIView.as_view(), name="history"),
    path("about/", CorrespondenceFacultyAboutAPIView.as_view(), name="about"),
]
