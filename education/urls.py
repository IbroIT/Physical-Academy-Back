from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    MasterDepartmentCategoriesAPIView,
    MasterDepartmentCategoryDetailAPIView,
    MasterFacultyManagementAPIView,
    PhdDepartmentCategoriesAPIView,
    PhdDepartmentCategoryDetailAPIView,
    PhdFacultyManagementAPIView,
    CollegeDepartmentCategoriesAPIView,
    CollegeDepartmentCategoryDetailAPIView,
    CollegeFacultyManagementAPIView,
)

urlpatterns = [
    path("master-categories/", MasterDepartmentCategoriesAPIView.as_view(), name="master-categories"),
    path(
        "master-categories/<int:id>/",
        MasterDepartmentCategoryDetailAPIView.as_view(),
        name="master-category-detail",
    ),
    path("master-management/", MasterFacultyManagementAPIView.as_view(), name="master-management"),
    path("phd-categories/", PhdDepartmentCategoriesAPIView.as_view(), name="phd-categories"),
    path(
        "phd-categories/<int:id>/",
        PhdDepartmentCategoryDetailAPIView.as_view(),
        name="phd-category-detail",
    ),
    path("phd-management/", PhdFacultyManagementAPIView.as_view(), name="phd-management"),
    path("college-categories/", CollegeDepartmentCategoriesAPIView.as_view(), name="college-categories"),
    path(
        "college-categories/<int:id>/",
        CollegeDepartmentCategoryDetailAPIView.as_view(),
        name="college-category-detail",
    ),
    path("college-management/", CollegeFacultyManagementAPIView.as_view(), name="college-management"),
]
