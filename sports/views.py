from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import SportSection, Achievement, Infrastructure
from .serializers import (
    SportSectionSerializer,
    AchievementSerializer,
    InfrastructureSerializer,
)


class SportSectionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для спортивных секций

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)
        - type: фильтр по типу спорта (game, combat, winter, water, athletics)
    """

    serializer_class = SportSectionSerializer

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return SportSection.objects.none()

        queryset = SportSection.objects.filter(is_active=True).prefetch_related(
            "translations", "training_schedules"
        )

        # Фильтрация по типу спорта
        sport_type = self.request.query_params.get("type", None)
        if sport_type:
            queryset = queryset.filter(sport_type=sport_type)

        return queryset.order_by("order", "coach_name")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class AchievementViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для спортивных достижений

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)
        - category: фильтр по категории (individual, team, international, olympic, coaching)
    """

    serializer_class = AchievementSerializer

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return Achievement.objects.none()

        queryset = Achievement.objects.filter(is_active=True).prefetch_related(
            "translations"
        )

        # Фильтрация по категории
        category = self.request.query_params.get("category", None)
        if category:
            queryset = queryset.filter(category=category)

        return queryset.order_by("-date", "order")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class InfrastructureViewSet(viewsets.ViewSet):
    """
    ViewSet для спортивной инфраструктуры

    Query Parameters:
        - lang: ru, en, kg (по умолчанию: ru)
    """

    serializer_class = (
        InfrastructureSerializer  # Default serializer for schema generation
    )
    queryset = Infrastructure.objects.none()  # Empty queryset for schema generation

    def list(self, request):
        """Получить информацию о спортивной инфраструктуре"""
        language = request.query_params.get("lang", "ru")

        # Получаем первую активную запись инфраструктуры
        infrastructure = (
            Infrastructure.objects.filter(is_active=True)
            .prefetch_related(
                "translations",
                "categories__translations",
                "categories__objects__translations",
            )
            .first()
        )

        if not infrastructure:
            return Response({"error": "Инфраструктура не найдена"}, status=404)

        serializer = InfrastructureSerializer(
            infrastructure, context={"language": language}
        )
        return Response(serializer.data)


# Дополнительные view для статистики


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
