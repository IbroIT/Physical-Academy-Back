from django.urls import path
from .views import (
    GeneralDepartmentsAPIRootView,
    DepartmentCategoriesAPIView,
    DepartmentCategoryDetailAPIView,
)

app_name = "general_departments"

urlpatterns = [
    path("", GeneralDepartmentsAPIRootView.as_view(), name="api-root"),
    path("categories/", DepartmentCategoriesAPIView.as_view(), name="categories"),
    path(
        "categories/<str:key>/",
        DepartmentCategoryDetailAPIView.as_view(),
        name="category-detail",
    ),
]
