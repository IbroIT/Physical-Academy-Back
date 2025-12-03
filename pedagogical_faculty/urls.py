from django.urls import path
from .views import (
    PedagogicalFacultyTabsAPIView,
    PedagogicalFacultyCardsAPIView,
    PedagogicalFacultyHistoryAPIView,
)

app_name = "pedagogical_faculty"

urlpatterns = [
    path("tabs/", PedagogicalFacultyTabsAPIView.as_view(), name="tabs"),
    path("cards/", PedagogicalFacultyCardsAPIView.as_view(), name="cards"),
    path("history/", PedagogicalFacultyHistoryAPIView.as_view(), name="history"),
]
