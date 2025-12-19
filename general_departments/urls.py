from django.urls import path
from .views import (
    GeneralDepartmentsAPIRootView,
    DepartmentCategoriesAPIView,
    DepartmentCategoryDetailAPIView,
    GeneralFacultyManagementAPIView,
    GeneralFacultyTabsAPIView,
)

app_name = "general_departments"

urlpatterns = [
    path("", GeneralDepartmentsAPIRootView.as_view(), name="api-root"),
    path("tabs/", GeneralFacultyTabsAPIView.as_view(), name="tabs"),
    path("categories/", DepartmentCategoriesAPIView.as_view(), name="categories"),
    path(
        "management/", GeneralFacultyManagementAPIView.as_view(), name="management"
    ),
    path(
        "categories/<str:key>/",
        DepartmentCategoryDetailAPIView.as_view(),
        name="category-detail",
    ),
]
