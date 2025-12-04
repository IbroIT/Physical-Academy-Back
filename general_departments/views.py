from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from .models import DepartmentCategory
from .serializers import (
    DepartmentCategorySerializer,
    DepartmentCategoryDetailSerializer,
)


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
            }
        )


class DepartmentCategoriesAPIView(APIView):
    """
    API для получения всех категорий кафедр

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)

    Returns:
        [
            {
                "id": 1,
                "key": "languages",
                "name": "Кафедра языков",
                "color": "blue-500",
                "description": "Описание кафедры...",
                "features": ["Особенность 1", "Особенность 2", "Особенность 3"],
                "order": 1
            }
        ]
    """

    def get(self, request):
        language = request.query_params.get("lang", "ru")

        categories = (
            DepartmentCategory.objects.filter(is_active=True)
            .select_related("info")
            .prefetch_related("features")
            .order_by("order")
        )

        serializer = DepartmentCategorySerializer(
            categories, many=True, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class DepartmentCategoryDetailAPIView(APIView):
    """
    API для получения детальной информации о категории

    URL Parameters:
        - key: ключ категории (languages, philosophy, fundamental, theory, pedagogy)

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)

    Returns:
        {
            "id": 1,
            "key": "languages",
            "name": "Кафедра языков",
            "color": "blue-500",
            "order": 1,
            "info": {
                "id": 1,
                "description": "Описание кафедры..."
            },
            "features": [
                {"id": 1, "feature": "Особенность 1", "order": 1},
                {"id": 2, "feature": "Особенность 2", "order": 2},
                {"id": 3, "feature": "Особенность 3", "order": 3}
            ]
        }
    """

    def get(self, request, key):
        language = request.query_params.get("lang", "ru")

        try:
            category = (
                DepartmentCategory.objects.select_related("info")
                .prefetch_related("features")
                .get(key=key, is_active=True)
            )
        except DepartmentCategory.DoesNotExist:
            return Response(
                {"error": f"Категория с ключом '{key}' не найдена"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = DepartmentCategoryDetailSerializer(
            category, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)
