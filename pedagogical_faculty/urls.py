from django.urls import path
from .views import (
    PedagogicalFacultyAPIRootView,
    PedagogicalFacultyTabsAPIView,
    PedagogicalFacultyCardsAPIView,
    PedagogicalFacultyHistoryAPIView,
    PedagogicalFacultyAboutAPIView,
    PedagogicalFacultyManagementAPIView,
    PedagogicalFacultySpecializationsAPIView,
    PedagogicalFacultyDepartmentsAPIView,
    DownloadResumeView,
)

app_name = "pedagogical_faculty"

urlpatterns = [
    path("", PedagogicalFacultyAPIRootView.as_view(), name="api-root"),
    path("tabs/", PedagogicalFacultyTabsAPIView.as_view(), name="tabs"),
    path("cards/", PedagogicalFacultyCardsAPIView.as_view(), name="cards"),
    path("history/", PedagogicalFacultyHistoryAPIView.as_view(), name="history"),
    path("about/", PedagogicalFacultyAboutAPIView.as_view(), name="about"),
    path(
        "management/", PedagogicalFacultyManagementAPIView.as_view(), name="management"
    ),
    path(
        "specializations/",
        PedagogicalFacultySpecializationsAPIView.as_view(),
        name="specializations",
    ),
    path(
        "departments/",
        PedagogicalFacultyDepartmentsAPIView.as_view(),
        name="departments",
    ),
    path(
        "resume/<str:model_type>/<int:pk>/",
        DownloadResumeView.as_view(),
        name="download-resume",
    ),
]
