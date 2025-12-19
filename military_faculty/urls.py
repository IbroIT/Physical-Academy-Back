from django.urls import path
from .views import (
    MilitaryFacultyAPIRootView,
    MilitaryFacultyTabsAPIView,
    MilitaryFacultyCardsAPIView,
    MilitaryFacultyHistoryAPIView,
    MilitaryFacultyAboutAPIView,
    MilitaryFacultyManagementAPIView,
    MilitaryFacultySpecializationsAPIView,
    MilitaryFacultyDepartmentsAPIView,
)

app_name = "military_faculty"

urlpatterns = [
    path("departments/", MilitaryFacultyDepartmentsAPIView.as_view(), name="departments"),
    path("tabs/", MilitaryFacultyTabsAPIView.as_view(), name="tabs"),
    path("cards/", MilitaryFacultyCardsAPIView.as_view(), name="cards"),
    path("history/", MilitaryFacultyHistoryAPIView.as_view(), name="history"),
    path("about/", MilitaryFacultyAboutAPIView.as_view(), name="about"),
    path("management/", MilitaryFacultyManagementAPIView.as_view(), name="management"),
    path(
        "specializations/",
        MilitaryFacultySpecializationsAPIView.as_view(),
        name="specializations",
    ),
]
