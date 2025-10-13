from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import (
    CollegeAdmissionSteps, CollegePrograms, CollegeSoonEvents, CollegeStatistics, DoctorPrograms, DoctorSoonEvents, DoctorStatistics, QuotaType, QuotaRequirement, QuotaBenefit, 
    QuotaStats, AdditionalSupport, ProcessStep,
    MasterDocuments, MasterPrograms, MasterMainDate, MasterRequirements,
    AspirantDocuments, AspirantPrograms, AspirantMainDate, AspirantRequirements,
    DoctorAdmissionSteps

)
from .serializers import (
    CollegeAdmissionStepsSerializer, CollegeProgramsFullSerializer, CollegeProgramsShortSerializer, CollegeSoonEventsSerializer, CollegeStatisticsSerializer, DoctorProgramsFullSerializer, DoctorProgramsShortSerializer, DoctorSoonEventsSerializer, DoctorStatisticsSerializer, DoctorStatisticsSerializer, QuotaTypeSerializer, QuotaRequirementSerializer, QuotaBenefitSerializer,
    QuotaStatsSerializer, AdditionalSupportSerializer, ProcessStepSerializer,
    BachelorQuotasDataSerializer, MasterDocumentsSerializer, MasterProgramsSerializer, 
    MasterMainDateSerializer, MasterRequirementsSerializer,
    AspirantDocumentsSerializer, AspirantProgramsSerializer, AspirantMainDateSerializer, 
    AspirantRequirementsSerializer, DoctorAdmissionStepsSerializer
)


class QuotaTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для типов квот"""

    serializer_class = QuotaTypeSerializer

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return QuotaType.objects.none()
        return (
            QuotaType.objects.filter(is_active=True)
            .prefetch_related("requirements", "benefits")
            .order_by("order", "type")
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class QuotaStatsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для статистики квот"""

    serializer_class = QuotaStatsSerializer

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return QuotaStats.objects.none()
        return QuotaStats.objects.filter(is_active=True).order_by("order")

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class AdditionalSupportViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для дополнительной поддержки"""

    serializer_class = AdditionalSupportSerializer

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return AdditionalSupport.objects.none()
        return AdditionalSupport.objects.filter(is_active=True).order_by("order")

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class ProcessStepViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для шагов процесса"""

    serializer_class = ProcessStepSerializer

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return ProcessStep.objects.none()
        return ProcessStep.objects.filter(is_active=True).order_by("step_number")

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class BachelorQuotasViewSet(viewsets.GenericViewSet):
    """Комплексный ViewSet для всех данных страницы бакалаврских квот"""

    serializer_class = (
        BachelorQuotasDataSerializer  # Default serializer for schema generation
    )
    queryset = QuotaType.objects.none()  # Empty queryset for schema generation

    @method_decorator(cache_page(60 * 15))  # Кэшируем на 15 минут
    def list(self, request):
        """
        Получить все данные для страницы бакалаврских квот (по умолчанию)

        Параметры:
        - lang: язык (ru, ky, en) - по умолчанию ru

        Возвращает структуру данных:
        {
            "quotas": [...],
            "quota_stats": [...],
            "additional_support": [...],
            "process_steps": [...]
        }
        """
        language = request.query_params.get("lang", "ru")

        # Валидируем язык
        if language not in ["ru", "ky", "en"]:
            language = "ru"

        serializer = BachelorQuotasDataSerializer({}, context={"language": language})

        return Response(serializer.data, status=status.HTTP_200_OK)

    @method_decorator(cache_page(60 * 15))  # Кэшируем на 15 минут
    @action(detail=False, methods=["get"], url_path="data")
    def get_bachelor_quotas_data(self, request):
        """
        Получить все данные для страницы бакалаврских квот

        Параметры:
        - lang: язык (ru, ky, en) - по умолчанию ru

        Возвращает структуру данных:
        {
            "quotas": [...],
            "quota_stats": [...],
            "additional_support": [...],
            "process_steps": [...]
        }
        """
        language = request.query_params.get("lang", "ru")

        # Валидируем язык
        if language not in ["ru", "ky", "en"]:
            language = "ru"

        serializer = BachelorQuotasDataSerializer({}, context={"language": language})

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="quotas-only")
    def get_quotas_only(self, request):
        """Получить только данные о квотах"""
        language = request.query_params.get("lang", "ru")

        if language not in ["ru", "ky", "en"]:
            language = "ru"

        quotas = (
            QuotaType.objects.filter(is_active=True)
            .prefetch_related("requirements", "benefits")
            .order_by("order", "type")
        )

        serializer = QuotaTypeSerializer(
            quotas, many=True, context={"language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="stats-only")
    def get_stats_only(self, request):
        """Получить только статистические данные"""
        language = request.query_params.get("lang", "ru")

        if language not in ["ru", "ky", "en"]:
            language = "ru"

        stats = QuotaStats.objects.filter(is_active=True).order_by("order")

        serializer = QuotaStatsSerializer(
            stats, many=True, context={"language": language}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class MasterDocumentsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для документов магистратуры"""

    serializer_class = MasterDocumentsSerializer
    queryset = MasterDocuments.objects.filter(is_active=True).order_by("order")

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return MasterDocuments.objects.none()
        return super().get_queryset().filter(is_active=True).order_by("order")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        # язык берём из query-параметра, например ?lang=en
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class MasterProgramsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для программ магистратуры"""

    serializer_class = MasterProgramsSerializer

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return MasterPrograms.objects.none()
        return super().get_queryset().filter(is_active=True).order_by("order")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        # язык берём из query-параметра, например ?lang=en
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class MasterMainDateViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для основных дат магистратуры"""

    serializer_class = MasterMainDateSerializer
    queryset = MasterMainDate.objects.filter(is_active=True).order_by("order")

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return MasterMainDate.objects.none()
        return super().get_queryset().filter(is_active=True).order_by("order")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        # язык берём из query-параметра, например ?lang=en
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class MasterRequirementsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для требований магистратуры"""

    serializer_class = MasterRequirementsSerializer
    queryset = MasterRequirements.objects.filter(is_active=True).order_by("order")

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return MasterRequirements.objects.none()
        return super().get_queryset().filter(is_active=True).order_by("order")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        # язык берём из query-параметра, например ?lang=en
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class AspirantDocumentsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для документов аспирантуры"""

    queryset = AspirantDocuments.objects.all()  # обязательно задать
    serializer_class = AspirantDocumentsSerializer

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return AspirantDocuments.objects.none()
        return super().get_queryset().filter(is_active=True).order_by("order")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        # язык берём из query-параметра, например ?lang=en
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class AspirantProgramsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для программ аспирантуры"""

    serializer_class = AspirantProgramsSerializer
    queryset = AspirantPrograms.objects.filter(is_active=True).order_by("order")

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return AspirantPrograms.objects.none()
        return super().get_queryset().filter(is_active=True).order_by("order")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        # язык берём из query-параметра, например ?lang=en
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class AspirantMainDateViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для основных дат аспирантуры"""

    serializer_class = AspirantMainDateSerializer
    queryset = AspirantMainDate.objects.filter(is_active=True).order_by("order")

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return AspirantMainDate.objects.none()
        return super().get_queryset().filter(is_active=True).order_by("order")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        # язык берём из query-параметра, например ?lang=en
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class AspirantRequirementsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для требований аспирантуры"""

    serializer_class = AspirantRequirementsSerializer
    queryset = AspirantRequirements.objects.filter(is_active=True).order_by("order")

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return AspirantRequirements.objects.none()
        return super().get_queryset().filter(is_active=True).order_by("order")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        # язык берём из query-параметра, например ?lang=en
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class DoctorAdmissionStepsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для шагов поступления в докторантуру"""

    serializer_class = DoctorAdmissionStepsSerializer
    queryset = DoctorAdmissionSteps.objects.filter(is_active=True).order_by("order")

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return DoctorAdmissionSteps.objects.none()
        return super().get_queryset().filter(is_active=True).order_by("order")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        # язык берём из query-параметра, например ?lang=en
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class DoctorStatisticsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для статистики докторантуры"""

    serializer_class = DoctorStatisticsSerializer
    queryset = DoctorStatistics.objects.order_by("id")

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return DoctorStatistics.objects.none()
        return super().get_queryset().order_by("id")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        # язык берём из query-параметра, например ?lang=en
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class DoctorProgramsViewSet(viewsets.ViewSet):
    """
    ViewSet для программ докторантуры.
    - GET /doctor-programs/ → список всех программ (короткая информация)
    - GET /doctor-programs/?id=<id> → полная информация по одной программе
    - Поддержка языков через query-параметр ?lang=<ru|ky|en>
    """

    serializer_class = (
        DoctorProgramsShortSerializer  # Default serializer for schema generation
    )
    queryset = DoctorPrograms.objects.none()  # Empty queryset for schema generation

    def list(self, request):
        program_id = request.query_params.get("id")
        language = request.query_params.get("lang", "ru")  # default 'ru'

        if program_id:
            # Получаем конкретную программу по id
            try:
                program = DoctorPrograms.objects.get(id=program_id)
            except DoctorPrograms.DoesNotExist:
                return Response({"detail": "Program not found"}, status=404)

            serializer = DoctorProgramsFullSerializer(
                program, context={"language": language}
            )
            return Response(serializer.data)
        else:
            # Список всех программ с короткой информацией
            programs = DoctorPrograms.objects.all()
            serializer = DoctorProgramsShortSerializer(
                programs, many=True, context={"language": language}
            )
            return Response(serializer.data)


class DoctorSoonEventsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для предстоящих событий докторантуры"""

    serializer_class = DoctorSoonEventsSerializer
    queryset = DoctorSoonEvents.objects.filter(is_active=True).order_by("date")

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return DoctorSoonEvents.objects.none()
        return super().get_queryset().filter(is_active=True).order_by("date")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        # язык берём из query-параметра, например ?lang=en
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class CollegeSoonEventsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для предстоящих событий колледжа"""

    serializer_class = CollegeSoonEventsSerializer
    queryset = CollegeSoonEvents.objects.filter(is_active=True).order_by("date")

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return CollegeSoonEvents.objects.none()
        return super().get_queryset().filter(is_active=True).order_by("date")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        # язык берём из query-параметра, например ?lang=en
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class CollegeProgramsViewSet(viewsets.ViewSet):
    """
    ViewSet для программ колледжа.
    - GET /college-programs/ → список всех программ (короткая информация)
    - GET /college-programs/?id=<id> → полная информация по одной программе
    - Поддержка языков через query-параметр ?lang=<ru|ky|en>
    """

    serializer_class = (
        CollegeProgramsShortSerializer  # Default serializer for schema generation
    )
    queryset = CollegePrograms.objects.none()  # Empty queryset for schema generation

    def list(self, request):
        program_id = request.query_params.get("id")
        language = request.query_params.get("lang", "ru")  # default 'ru'

        if program_id:
            # Получаем конкретную программу по id
            try:
                program = CollegePrograms.objects.get(id=program_id)
            except CollegePrograms.DoesNotExist:
                return Response({"detail": "Program not found"}, status=404)

            serializer = CollegeProgramsFullSerializer(
                program, context={"language": language}
            )
            return Response(serializer.data)
        else:
            # Список всех программ с короткой информацией
            programs = CollegePrograms.objects.all()
            serializer = CollegeProgramsShortSerializer(
                programs, many=True, context={"language": language}
            )
            return Response(serializer.data)


class CollegeAdmissionStepsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для шагов поступления в колледж"""

    serializer_class = CollegeAdmissionStepsSerializer
    queryset = CollegeAdmissionSteps.objects.order_by("order")

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return CollegeAdmissionSteps.objects.none()
        return super().get_queryset().order_by("order")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        # язык берём из query-параметра, например ?lang=en
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class CollegeAdmissionRequirementsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для требований поступления в колледж"""

    serializer_class = CollegeAdmissionStepsSerializer
    queryset = CollegeAdmissionSteps.objects.filter(is_active=True)

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return CollegeAdmissionSteps.objects.none()
        return super().get_queryset().filter(is_active=True)

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        # язык берём из query-параметра, например ?lang=en
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context


class CollegeStatisticsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для статистики колледжа"""

    serializer_class = CollegeStatisticsSerializer
    queryset = CollegeStatistics.objects.order_by("id")

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return CollegeStatistics.objects.none()
        return super().get_queryset().order_by("id")

    def get_serializer_context(self):
        """Передаём язык в контекст сериализатора"""
        context = super().get_serializer_context()
        # язык берём из query-параметра, например ?lang=en
        language = self.request.query_params.get("lang", "ru")
        context["language"] = language
        return context