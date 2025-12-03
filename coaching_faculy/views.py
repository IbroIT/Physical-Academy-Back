from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TabCategory, TimelineEvent
from .serializers import (
    TabCategorySerializer,
    TimelineEventSerializer,
    FacultyDataSerializer,
)


class CoachingFacultyDataAPIView(APIView):
    """
    API для получения всех данных тренерского факультета

    Query Parameters:
        - language: ru, en, kg (по умолчанию: ru)

    Returns:
        {
            "tabs": [...],  # категории с карточками
            "timeline": [...]  # события истории
        }
    """

    def get(self, request):
        # Получаем язык из query params
        language = request.query_params.get("lang", "ru")

        # Получаем все активные табы с карточками
        tabs = (
            TabCategory.objects.filter(is_active=True)
            .prefetch_related("cards")
            .order_by("order")
        )

        # Получаем все активные события истории
        timeline = TimelineEvent.objects.filter(is_active=True).order_by("order")

        # Сериализуем данные с передачей языка в контекст
        tabs_serializer = TabCategorySerializer(
            tabs, many=True, context={"request": request, "language": language}
        )
        timeline_serializer = TimelineEventSerializer(
            timeline, many=True, context={"request": request, "language": language}
        )

        response_data = {
            "tabs": tabs_serializer.data,
            "timeline": timeline_serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)
