from django.urls import path
from .views import (
    CorrespondenceFacultyTabsAPIView,
    CorrespondenceFacultyCardsAPIView,
    CorrespondenceFacultyHistoryAPIView,
)

app_name = "correspondence_faculty"

urlpatterns = [
    path("tabs/", CorrespondenceFacultyTabsAPIView.as_view(), name="tabs"),
    path("cards/", CorrespondenceFacultyCardsAPIView.as_view(), name="cards"),
    path("history/", CorrespondenceFacultyHistoryAPIView.as_view(), name="history"),
]
