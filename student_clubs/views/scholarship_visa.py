from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from ..models_scholarship_visa import (
    ScholarshipProgram,
    ScholarshipRequiredDocument,
    VisaSupportService,
    VisaSupportContact,
)
from ..serializers_scholarship_visa import (
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
    list=extend_schema(description="Получить список всех необходимых документов")
)
class ScholarshipRequiredDocumentViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для документов, необходимых для стипендий"""

    queryset = ScholarshipRequiredDocument.objects.all().order_by("order")
    serializer_class = ScholarshipRequiredDocumentSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "ru")
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"
        context["language"] = lang
        return context


@extend_schema_view(
    list=extend_schema(description="Получить все данные для страницы о стипендиях")
)
class ScholarshipPageDataViewSet(viewsets.ViewSet):
    """ViewSet для получения всех данных для страницы о стипендиях"""

    permission_classes = [permissions.AllowAny]

    @method_decorator(cache_page(60 * 15))  # 15 min cache
    def list(self, request):
        # Получаем язык
        lang = self.request.query_params.get("lang", "ru")
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"

        # Получаем данные
        programs = ScholarshipProgram.objects.filter(is_active=True).order_by("name_ru")
        documents = ScholarshipRequiredDocument.objects.all().order_by("order")

        # Сериализуем данные
        serializer = ScholarshipPageDataSerializer(
            {"programs": programs, "documents": documents},
            context={"request": request, "language": lang},
        )
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(description="Получить список всех визовых услуг")
)
class VisaSupportServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для визовых услуг"""

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


@extend_schema_view(
    list=extend_schema(
        description="Получить список всех контактов для визовой поддержки"
    )
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


@extend_schema_view(
    list=extend_schema(
        description="Получить все данные для страницы о визовой поддержке"
    )
)
class VisaSupportPageDataViewSet(viewsets.ViewSet):
    """ViewSet для получения всех данных для страницы о визовой поддержке"""

    permission_classes = [permissions.AllowAny]

    @method_decorator(cache_page(60 * 15))  # 15 min cache
    def list(self, request):
        # Получаем язык
        lang = self.request.query_params.get("lang", "ru")
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"

        # Получаем данные
        services = VisaSupportService.objects.filter(is_active=True).order_by("order")
        contacts = VisaSupportContact.objects.filter(is_active=True).order_by("order")

        # Сериализуем данные
        serializer = VisaSupportPageDataSerializer(
            {"services": services, "contacts": contacts},
            context={"request": request, "language": lang},
        )
        return Response(serializer.data)
