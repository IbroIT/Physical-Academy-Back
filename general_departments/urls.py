from django.urls import path
from .views import (
    GeneralDepartmentsAPIRootView,
    DepartmentCategoriesAPIView,
    DepartmentCategoryDetailAPIView,
    GeneralFacultyManagementAPIView,
)

app_name = "general_departments"

urlpatterns = [
    path("", GeneralDepartmentsAPIRootView.as_view(), name="api-root"),
    path("categories/", DepartmentCategoriesAPIView.as_view(), name="categories"),
    path(
        "categories/<int:id>/",
        DepartmentCategoryDetailAPIView.as_view(),
        name="category-detail",
    ),
    path("management/", GeneralFacultyManagementAPIView.as_view(), name="management"),
]
