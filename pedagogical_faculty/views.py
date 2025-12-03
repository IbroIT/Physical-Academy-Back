from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TabCategory
from .serializers import TabCategorySerializer, FacultyDataSerializer


class PedagogicalFacultyDataAPIView(APIView):
    """
    API для получения всех данных педагогического факультета

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)

    Returns:
        {
            "tabs": [
                {
                    "key": "history",
                    "title": "История",
                    "cards": [],
                    "timeline_events": [{"year": "1990", "event": "..."}]
                },
                {
                    "key": "about",
                    "title": "О факультете",
                    "cards": [{"title": "...", "description": "..."}],
                    "timeline_events": []
                }
            ]
        }
    """

    def get(self, request):
        # Получаем язык из query params
        language = request.query_params.get("lang", "ru")

        # Получаем все активные табы с карточками и timeline_events
        tabs = (
            TabCategory.objects.filter(is_active=True)
            .prefetch_related("cards", "timeline_events")
            .order_by("order")
        )

        # Сериализуем данные с передачей языка в контекст
        serializer = FacultyDataSerializer(
            {"tabs": tabs}, context={"request": request, "language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)
