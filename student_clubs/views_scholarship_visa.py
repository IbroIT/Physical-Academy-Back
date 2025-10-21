from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models_scholarship_visa import (
    ScholarshipProgram,
    ScholarshipRequiredDocument,
    VisaSupportService,
    VisaSupportContact,
)
from .serializers_scholarship_visa import (
    ScholarshipProgramSerializer,
    ScholarshipRequiredDocumentSerializer,
    ScholarshipPageDataSerializer,
    VisaSupportServiceSerializer,
    VisaSupportContactSerializer,
    VisaSupportPageDataSerializer,
)


@extend_schema_view(
    list=extend_schema(description="Получить список всех стипендиальных программ"),
    retrieve=extend_schema(
        description="Получить детальную информацию о стипендиальной программе"
    ),
)
class ScholarshipProgramViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для стипендиальных программ"""

    queryset = ScholarshipProgram.objects.filter(is_active=True).order_by("name_ru")
    serializer_class = ScholarshipProgramSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "ru")
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"
        context["language"] = lang
        return context


@extend_schema_view(
    list=extend_schema(description="Получить список документов для стипендии"),
    retrieve=extend_schema(
        description="Получить детальную информацию о требуемом документе"
    ),
)
class ScholarshipRequiredDocumentViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для документов для стипендии"""

    queryset = ScholarshipRequiredDocument.objects.all().order_by(
        "scholarship", "order"
    )
    serializer_class = ScholarshipRequiredDocumentSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "ru")
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"
        context["language"] = lang
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        scholarship_id = self.request.query_params.get("scholarship_id")
        if scholarship_id:
            queryset = queryset.filter(scholarship_id=scholarship_id)
        return queryset


@extend_schema_view(
    list=extend_schema(description="Получить список сервисов визовой поддержки"),
    retrieve=extend_schema(
        description="Получить детальную информацию о сервисе визовой поддержки"
    ),
)
class VisaSupportServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для сервисов визовой поддержки"""

    queryset = VisaSupportService.objects.filter(is_active=True).order_by("order")
    serializer_class = VisaSupportServiceSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "ru")
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"
        context["language"] = lang
        return context

    @action(detail=False, methods=["get"])
    @method_decorator(cache_page(60 * 15))  # Кэширование на 15 минут
    def featured(self, request):
        """Получить выделенные сервисы"""
        queryset = self.get_queryset().filter(is_featured=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(description="Получить список контактов визовой поддержки"),
    retrieve=extend_schema(
        description="Получить детальную информацию о контакте визовой поддержки"
    ),
)
class VisaSupportContactViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для контактов визовой поддержки"""

    queryset = VisaSupportContact.objects.filter(is_active=True).order_by("order")
    serializer_class = VisaSupportContactSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "ru")
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"
        context["language"] = lang
        return context


class ScholarshipPageDataViewSet(viewsets.ViewSet):
    """ViewSet для получения данных для страницы стипендий"""

    permission_classes = [permissions.AllowAny]

    @extend_schema(
        description="Получить все данные для страницы стипендий",
        responses={200: ScholarshipPageDataSerializer},
    )
    @method_decorator(cache_page(60 * 15))  # Кэширование на 15 минут
    def list(self, request):
        """Получить все данные для страницы стипендий"""
        lang = request.query_params.get("lang", "ru")
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"

        serializer = ScholarshipPageDataSerializer(
            instance=None, context={"language": lang, "request": request}
        )

        return Response(serializer.data)


class VisaSupportPageDataViewSet(viewsets.ViewSet):
    """ViewSet для получения данных для страницы визовой поддержки"""

    permission_classes = [permissions.AllowAny]

    @extend_schema(
        description="Получить все данные для страницы визовой поддержки",
        responses={200: VisaSupportPageDataSerializer},
    )
    @method_decorator(cache_page(60 * 15))  # Кэширование на 15 минут
    def list(self, request):
        """Получить все данные для страницы визовой поддержки"""
        lang = request.query_params.get("lang", "ru")
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"

        serializer = VisaSupportPageDataSerializer(
            instance=None, context={"language": lang, "request": request}
        )

        return Response(serializer.data)
