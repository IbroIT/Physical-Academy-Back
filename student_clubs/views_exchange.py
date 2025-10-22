from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models_exchange import (
    ExchangeRegion,
    ExchangeDurationType,
    ExchangeProgram,
    ExchangeProgramRequirement,
    ExchangeProgramBenefit,
    ExchangeProgramCourse,
    ExchangePageStat,
    ExchangeDeadline,
)
from .serializers_exchange import (
    ExchangeRegionSerializer,
    ExchangeDurationTypeSerializer,
    ExchangeProgramSerializer,
    ExchangeProgramRequirementSerializer,
    ExchangeProgramBenefitSerializer,
    ExchangeProgramCourseSerializer,
    ExchangePageStatSerializer,
    ExchangeDeadlineSerializer,
    ExchangePageDataSerializer,
)


class ExchangeRegionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для регионов программ обмена.
    """

    queryset = ExchangeRegion.objects.all()
    serializer_class = ExchangeRegionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExchangeDurationTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для типов длительности программ обмена.
    """

    queryset = ExchangeDurationType.objects.all()
    serializer_class = ExchangeDurationTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExchangeProgramViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для программ обмена.
    """

    queryset = ExchangeProgram.objects.filter(is_active=True)
    serializer_class = ExchangeProgramSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        language = self.request.query_params.get("lang", "en")
        if language not in ["en", "ru", "kg"]:
            language = "en"
        context["language"] = language
        return context


class ExchangeProgramRequirementViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для требований программ обмена.
    """

    queryset = ExchangeProgramRequirement.objects.all()
    serializer_class = ExchangeProgramRequirementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ["program"]


class ExchangeProgramBenefitViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для преимуществ программ обмена.
    """

    queryset = ExchangeProgramBenefit.objects.all()
    serializer_class = ExchangeProgramBenefitSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ["program"]


class ExchangeProgramCourseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для доступных курсов в программах обмена.
    """

    queryset = ExchangeProgramCourse.objects.all()
    serializer_class = ExchangeProgramCourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ["program"]


class ExchangePageStatViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для статистики на странице программ обмена.
    """

    queryset = ExchangePageStat.objects.all().order_by("order")
    serializer_class = ExchangePageStatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExchangeDeadlineViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для дедлайнов программ обмена.
    """

    queryset = ExchangeDeadline.objects.all().order_by("order")
    serializer_class = ExchangeDeadlineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExchangePageDataViewSet(viewsets.ViewSet):
    """
    API endpoint для получения полных данных для страницы программ обмена.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request):
        language = request.query_params.get("lang", "en")
        if language not in ["en", "ru", "kg"]:
            language = "en"

        serializer = ExchangePageDataSerializer(
            {"request": request}, context={"language": language, "request": request}
        )
        return Response(serializer.data)
