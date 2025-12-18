from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
import mimetypes
from .models import (
    TabCategory,
    Card,
    TimelineEvent,
    AboutFaculty,
    Management,
    Specialization,
    Department,
    DepartmentStaff,
)
from .serializers import (
    TabCategorySerializer,
    CardSerializer,
    TimelineEventSerializer,
    AboutFacultySerializer,
    ManagementSerializer,
    SpecializationSerializer,
    DepartmentSerializer,
)


class PedagogicalFacultyAPIRootView(APIView):
    """
    Корневой API эндпоинт педагогического факультета
    Показывает все доступные эндпоинты
    """

    def get(self, request, format=None):
        return Response(
            {
                "tabs": reverse(
                    "pedagogical_faculty:tabs", request=request, format=format
                ),
                "cards": reverse(
                    "pedagogical_faculty:cards", request=request, format=format
                ),
                "history": reverse(
                    "pedagogical_faculty:history", request=request, format=format
                ),
                "about": reverse(
                    "pedagogical_faculty:about", request=request, format=format
                ),
                "management": reverse(
                    "pedagogical_faculty:management", request=request, format=format
                ),
                "specializations": reverse(
                    "pedagogical_faculty:specializations",
                    request=request,
                    format=format,
                ),
                "departments": reverse(
                    "pedagogical_faculty:departments", request=request, format=format
                ),
            }
        )


class PedagogicalFacultyTabsAPIView(APIView):
    """
    API для получения всех табов (категорий) педагогического факультета

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)

    Returns:
        [
            {"id": 1, "key": "history", "title": "История", "icon": "📜", "order": 1},
            {"id": 2, "key": "about", "title": "О факультете", "icon": "ℹ️", "order": 2}
        ]
    """

    def get(self, request):
        language = request.query_params.get("lang", "ru")

        tabs = TabCategory.objects.filter(is_active=True).order_by("order")
        serializer = TabCategorySerializer(
            tabs, many=True, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class PedagogicalFacultyCardsAPIView(APIView):
    """
    API для получения карточек для конкретного таба

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)
        - tab: key таба (например: about, management) - обязательный параметр

    Returns:
        [
            {"id": 1, "title": "Миссия", "description": "Текст...", "order": 1},
            {"id": 2, "title": "Цели", "description": "Текст...", "order": 2}
        ]
    """

    def get(self, request):
        language = request.query_params.get("lang", "ru")
        tab_key = request.query_params.get("tab")

        if not tab_key:
            return Response(
                {"error": "Параметр 'tab' обязателен"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            tab = TabCategory.objects.get(key=tab_key, is_active=True)
        except TabCategory.DoesNotExist:
            return Response(
                {"error": f"Таб с ключом '{tab_key}' не найден"},
                status=status.HTTP_404_NOT_FOUND,
            )

        cards = Card.objects.filter(tab=tab, is_active=True).order_by("order")
        serializer = CardSerializer(
            cards, many=True, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class PedagogicalFacultyHistoryAPIView(APIView):
    """
    API для получения событий истории (timeline)

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)

    Returns:
        [
            {"id": 1, "year": "1990", "event": "Основание академии", "order": 1},
            {"id": 2, "year": "2000", "event": "Получение аккредитации", "order": 2}
        ]
    """

    def get(self, request):
        language = request.query_params.get("lang", "ru")

        # Получаем таб с ключом history
        try:
            history_tab = TabCategory.objects.get(key="history", is_active=True)
            timeline = TimelineEvent.objects.filter(
                tab=history_tab, is_active=True
            ).order_by("order")
        except TabCategory.DoesNotExist:
            # Если таб history не найден, возвращаем пустой список
            timeline = TimelineEvent.objects.none()

        serializer = TimelineEventSerializer(
            timeline, many=True, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class PedagogicalFacultyAboutAPIView(APIView):
    """API для получения текста 'О факультете' (about_faculty)"""

    def get(self, request):
        language = request.query_params.get("lang", "ru")

        try:
            about_tab = TabCategory.objects.get(key="about_faculty", is_active=True)
            items = AboutFaculty.objects.filter(tab=about_tab, is_active=True).order_by(
                "order"
            )
        except TabCategory.DoesNotExist:
            items = AboutFaculty.objects.none()

        serializer = AboutFacultySerializer(
            items, many=True, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class PedagogicalFacultyManagementAPIView(APIView):
    """API для получения руководства факультета (management)

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)
    """

    def get(self, request):
        language = request.query_params.get("lang", "ru")

        try:
            management_tab = TabCategory.objects.get(key="management", is_active=True)
            items = Management.objects.filter(
                tab=management_tab, is_active=True
            ).order_by("order")
        except TabCategory.DoesNotExist:
            items = Management.objects.none()

        serializer = ManagementSerializer(
            items, many=True, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class PedagogicalFacultySpecializationsAPIView(APIView):
    """API для получения специализаций факультета (specializations)

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)
    """

    def get(self, request):
        language = request.query_params.get("lang", "ru")

        try:
            spec_tab = TabCategory.objects.get(key="specializations", is_active=True)
            items = Specialization.objects.filter(
                tab=spec_tab, is_active=True
            ).order_by("order")
        except TabCategory.DoesNotExist:
            items = Specialization.objects.none()

        serializer = SpecializationSerializer(
            items, many=True, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class PedagogicalFacultyDepartmentsAPIView(APIView):
    """API для получения кафедр факультета с сотрудниками (departments)

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)
    """

    def get(self, request):
        language = request.query_params.get("lang", "ru")

        try:
            dept_tab = TabCategory.objects.get(key="departments", is_active=True)
            items = Department.objects.filter(tab=dept_tab, is_active=True).order_by(
                "order"
            )
        except TabCategory.DoesNotExist:
            items = Department.objects.none()

        serializer = DepartmentSerializer(
            items, many=True, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class DownloadResumeView(APIView):
    """
    View для скачивания резюме управления и сотрудников кафедр
    """
    def get(self, request, model_type, pk):
        # Определяем модель по типу
        if model_type == "management":
            obj = get_object_or_404(Management, pk=pk, is_active=True)
        elif model_type == "staff":
            obj = get_object_or_404(DepartmentStaff, pk=pk, is_active=True)
        else:
            raise Http404("Invalid model type")
        
        # Проверяем наличие резюме
        if not obj.resume:
            raise Http404("Resume not found")
        
        try:
            # Получаем файл
            file_content = obj.resume.read()
            
            # Определяем MIME тип
            content_type = mimetypes.guess_type(obj.resume.name)[0] or 'application/pdf'
            
            # Создаем ответ с файлом
            response = HttpResponse(file_content, content_type=content_type)
            response['Content-Disposition'] = f'inline; filename="{obj.resume.name.split("/")[-1]}"'
            
            return response
        except Exception as e:
            raise Http404(f"Error reading file: {str(e)}")
