from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import SportSection, Achievement, Infrastructure
from .serializers import (
    SportSectionSerializer,
    AchievementSerializer,
    InfrastructureSerializer,
)


class SportSectionListAPIView(generics.ListAPIView):
    """
    API для получения списка спортивных секций

    Query Parameters:
        - language: ru, en, kg (по умолчанию: ru)
        - type: фильтр по типу спорта (game, combat, winter, water, athletics)
    """

    serializer_class = SportSectionSerializer

    def get_queryset(self):
        # translations table was removed; use per-field translation columns.
        queryset = SportSection.objects.filter(is_active=True).prefetch_related(
            "training_schedules"
        )

        # Фильтрация по типу спорта
        sport_type = self.request.query_params.get("type", None)
        if sport_type:
            queryset = queryset.filter(sport_type=sport_type)

        return queryset.order_by("order", "coach_name")

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)


class SportSectionDetailAPIView(generics.RetrieveAPIView):
    """
    API для получения детальной информации о спортивной секции

    Query Parameters:
        - language: ru, en, kg (по умолчанию: ru)
    """

    serializer_class = SportSectionSerializer
    lookup_field = "id"

    def get_queryset(self):
        return SportSection.objects.filter(is_active=True).prefetch_related(
            "training_schedules"
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={"request": request})
        return Response(serializer.data)


class AchievementListAPIView(generics.ListAPIView):
    """
    API для получения списка спортивных достижений

    Query Parameters:
        - language: ru, en, kg (по умолчанию: ru)
        - category: фильтр по категории (individual, team, international, olympic, coaching)
    """

    serializer_class = AchievementSerializer

    def get_queryset(self):
        # Achievement uses per-field description_* translations now.
        queryset = Achievement.objects.filter(is_active=True)

        # Фильтрация по категории
        category = self.request.query_params.get("category", None)
        if category:
            queryset = queryset.filter(category=category)

        return queryset.order_by("-date", "order")

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)


class AchievementDetailAPIView(generics.RetrieveAPIView):
    """
    API для получения детальной информации о достижении

    Query Parameters:
        - language: ru, en, kg (по умолчанию: ru)
    """

    serializer_class = AchievementSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Achievement.objects.filter(is_active=True)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={"request": request})
        return Response(serializer.data)


class InfrastructureAPIView(APIView):
    """
    API для получения информации о спортивной инфраструктуре

    Query Parameters:
        - language: ru, en, kg (по умолчанию: ru)
    """

    def get(self, request):
        # Получаем первую активную запись инфраструктуры
        # Prefetch related categories, objects and statistics. The old
        # "translations" relations were removed in favor of per-field columns.
        infrastructure = (
            Infrastructure.objects.filter(is_active=True)
            .prefetch_related(
                "categories",
                "categories__objects",
                "statistics",
            )
            .first()
        )

        if not infrastructure:
            return Response({"error": "Инфраструктура не найдена"}, status=404)

        serializer = InfrastructureSerializer(
            infrastructure, context={"request": request}
        )
        return Response(serializer.data)


# Дополнительные view для статистики и фильтрации


class SportStatisticsAPIView(APIView):
    """
    API для получения общей статистики по спорту
    """

    def get(self, request):
        from django.db.models import Count

        sections_count = SportSection.objects.filter(is_active=True).count()
        achievements_count = Achievement.objects.filter(is_active=True).count()

        # Статистика по типам спорта
        sections_by_type = (
            SportSection.objects.filter(is_active=True)
            .values("sport_type")
            .annotate(count=Count("id"))
        )

        # Статистика по категориям достижений
        achievements_by_category = (
            Achievement.objects.filter(is_active=True)
            .values("category")
            .annotate(count=Count("id"))
        )

        return Response(
            {
                "total_sections": sections_count,
                "total_achievements": achievements_count,
                "sections_by_type": list(sections_by_type),
                "achievements_by_category": list(achievements_by_category),
            }
        )
