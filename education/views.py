from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework import generics

from .models import MasterTabCategory, MasterManagement, PhdTabCategory, PhdManagement, CollegeTabCategory, CollegeManagement
from .serializers import (
    MasterDepartmentCategorySerializer,
    MasterDepartmentCategoryDetailSerializer,
    MasterManagementSerializer,
    PhdDepartmentCategorySerializer,
    PhdDepartmentCategoryDetailSerializer,
    PhdManagementSerializer,
    CollegeDepartmentCategorySerializer,
    CollegeDepartmentCategoryDetailSerializer,
    CollegeManagementSerializer,
)


class CollegeFacultyManagementAPIView(APIView):
    """API для получения руководства факультета (management)

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)
    """

    def get(self, request):
        language = request.query_params.get("lang", "ru")

        # Получаем все активные записи руководства
        items = CollegeManagement.objects.filter(is_active=True).order_by("order")

        serializer = CollegeManagementSerializer(
            items, many=True, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class CollegeDepartmentCategoriesAPIView(generics.ListAPIView):
    """API для получения списка категорий кафедр"""

    queryset = CollegeTabCategory.objects.filter(is_active=True).order_by("order")
    serializer_class = CollegeDepartmentCategorySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context

    

class CollegeDepartmentCategoryDetailAPIView(APIView):
    """API для получения детальной информации о категории кафедры"""

    def get(self, request, id):
        language = request.query_params.get("lang", "ru")

        try:
            category = (
                CollegeTabCategory.objects.select_related("info")
                .prefetch_related("management")
                .get(id=id, is_active=True)
            )
        except CollegeTabCategory.DoesNotExist:
            return Response(
                {"error": f"Категория с id '{id}' не найдена"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = CollegeDepartmentCategoryDetailSerializer(
            category, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)




class MasterFacultyManagementAPIView(APIView):
    """API для получения руководства факультета (management)

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)
    """

    def get(self, request):
        language = request.query_params.get("lang", "ru")

        # Получаем все активные записи руководства
        items = MasterManagement.objects.filter(is_active=True).order_by("order")

        serializer = MasterManagementSerializer(
            items, many=True, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class MasterDepartmentCategoriesAPIView(generics.ListAPIView):
    """API для получения списка категорий кафедр"""

    queryset = MasterTabCategory.objects.filter(is_active=True).order_by("order")
    serializer_class = MasterDepartmentCategorySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context

    

class MasterDepartmentCategoryDetailAPIView(APIView):
    """API для получения детальной информации о категории кафедры"""

    def get(self, request, id):
        language = request.query_params.get("lang", "ru")

        try:
            category = (
                MasterTabCategory.objects.select_related("info")
                .prefetch_related("management")
                .get(id=id, is_active=True)
            )
        except MasterTabCategory.DoesNotExist:
            return Response(
                {"error": f"Категория с id '{id}' не найдена"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = MasterDepartmentCategoryDetailSerializer(
            category, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class PhdFacultyManagementAPIView(APIView):
    """API для получения руководства факультета (management)

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)
    """

    def get(self, request):
        language = request.query_params.get("lang", "ru")

        # Получаем все активные записи руководства
        items = PhdManagement.objects.filter(is_active=True).order_by("order")

        serializer = PhdManagementSerializer(
            items, many=True, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)





class PhdDepartmentCategoriesAPIView(generics.ListAPIView):
    """API для получения списка категорий кафедр"""

    queryset = PhdTabCategory.objects.filter(is_active=True).order_by("order")
    serializer_class = PhdDepartmentCategorySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context

    

class PhdDepartmentCategoryDetailAPIView(APIView):
    """API для получения детальной информации о категории кафедры"""

    def get(self, request, id):
        language = request.query_params.get("lang", "ru")

        try:
            category = (
                PhdTabCategory.objects.select_related("info")
                .prefetch_related("management")
                .get(id=id, is_active=True)
            )
        except PhdTabCategory.DoesNotExist:
            return Response(
                {"error": f"Категория с id '{id}' не найдена"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = PhdDepartmentCategoryDetailSerializer(
            category, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)
