from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework import generics

from .models import TabCategory, Management
from .serializers import (
    DepartmentCategorySerializer,
    DepartmentCategoryDetailSerializer,
    ManagementSerializer,
)




class GeneralFacultyManagementAPIView(APIView):
    """API для получения руководства факультета (management)

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)
    """

    def get(self, request):
        language = request.query_params.get("lang", "ru")

        # Получаем все активные записи руководства
        items = Management.objects.filter(is_active=True).order_by("order")

        serializer = ManagementSerializer(
            items, many=True, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)



class GeneralDepartmentsAPIRootView(APIView):
    """
    Корневой API эндпоинт общих кафедр
    Показывает все доступные эндпоинты
    """

    def get(self, request, format=None):
        return Response(
            {
                "categories": reverse(
                    "general_departments:categories", request=request, format=format
                ),
                "management": reverse(
                    "general_departments:management", request=request, format=format
                ),
            }
        )


class DepartmentCategoriesAPIView(generics.ListAPIView):
    """API для получения списка категорий кафедр"""

    queryset = TabCategory.objects.filter(is_active=True).order_by("order")
    serializer_class = DepartmentCategorySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context

    

class DepartmentCategoryDetailAPIView(APIView):
    """API для получения детальной информации о категории кафедры"""

    def get(self, request, id):
        language = request.query_params.get("lang", "ru")

        try:
            category = (
                TabCategory.objects.select_related("info")
                .prefetch_related("management")
                .get(id=id, is_active=True)
            )
        except TabCategory.DoesNotExist:
            return Response(
                {"error": f"Категория с id '{id}' не найдена"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = DepartmentCategoryDetailSerializer(
            category, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)
