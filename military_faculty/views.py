from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from .models import (
    TabCategory,
    Card,
    TimelineEvent,
    AboutFaculty,
    Management,
    Specialization,
    Department,
)
from .serializers import (
    TabCategorySerializer,
    CardSerializer,
    TimelineEventSerializer,
    AboutFacultySerializer,
    ManagementSerializer,
    DepartmentSerializer,
    SpecializationSerializer,
)


class MilitaryFacultyDepartmentsAPIView(APIView):
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




class MilitaryFacultyAPIRootView(APIView):
    """
    Корневой API эндпоинт военного факультета
    Показывает все доступные эндпоинты
    """

    def get(self, request, format=None):
        return Response(
            {
                "tabs": reverse(
                    "military_faculty:tabs", request=request, format=format
                ),
                "cards": reverse(
                    "military_faculty:cards", request=request, format=format
                ),
                "history": reverse(
                    "military_faculty:history", request=request, format=format
                ),
                "about": reverse(
                    "military_faculty:about", request=request, format=format
                ),
                "management": reverse(
                    "military_faculty:management", request=request, format=format
                ),
                "specializations": reverse(
                    "military_faculty:specializations", request=request, format=format
                ),
            }
        )


class MilitaryFacultyTabsAPIView(APIView):
    """
    API для получения всех табов (категорий) военного факультета

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


class MilitaryFacultyCardsAPIView(APIView):
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


class MilitaryFacultyHistoryAPIView(APIView):
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


class MilitaryFacultyAboutAPIView(APIView):
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


class MilitaryFacultyManagementAPIView(APIView):
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


class MilitaryFacultySpecializationsAPIView(APIView):
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
