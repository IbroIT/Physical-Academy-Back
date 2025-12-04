from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from .models import TabCategory, Card, TimelineEvent
from .serializers import TabCategorySerializer, CardSerializer, TimelineEventSerializer


class CoachingFacultyAPIRootView(APIView):
    """
    Корневой API эндпоинт тренерского факультета
    Показывает все доступные эндпоинты
    """

    def get(self, request, format=None):
        return Response(
            {
                "tabs": reverse(
                    "coaching_faculty:tabs", request=request, format=format
                ),
                "cards": reverse(
                    "coaching_faculty:cards", request=request, format=format
                ),
                "history": reverse(
                    "coaching_faculty:history", request=request, format=format
                ),
            }
        )


class CoachingFacultyTabsAPIView(APIView):
    """
    API для получения всех табов (категорий) тренерского факультета

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


class CoachingFacultyCardsAPIView(APIView):
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


class CoachingFacultyHistoryAPIView(APIView):
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
