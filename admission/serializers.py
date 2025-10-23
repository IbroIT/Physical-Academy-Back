from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from .models import (
    CollegeAdmissionRequirements,
    CollegeAdmissionSteps,
    CollegePrograms,
    CollegeSoonEvents,
    CollegeStatistics,
    DoctorSoonEvents,
    QuotaType,
    QuotaRequirement,
    QuotaBenefit,
    QuotaStats,
    AdditionalSupport,
    ProcessStep,
    AspirantDocuments,
    AspirantMainDate,
    AspirantPrograms,
    AspirantRequirements,
    MasterDocuments,
    MasterMainDate,
    MasterPrograms,
    MasterRequirements,
    DoctorAdmissionSteps,
    DoctorStatistics,
    DoctorPrograms,
    BachelorProgram,
)


class QuotaRequirementSerializer(serializers.ModelSerializer):
    """Сериализатор для требований к квотам"""

    requirement = serializers.SerializerMethodField()

    class Meta:
        model = QuotaRequirement
        fields = ["id", "requirement", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_requirement(self, obj) -> str:
        """Получить требование на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_requirement(language)


class QuotaBenefitSerializer(serializers.ModelSerializer):
    """Сериализатор для преимуществ квот"""

    benefit = serializers.SerializerMethodField()

    class Meta:
        model = QuotaBenefit
        fields = ["id", "benefit", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_benefit(self, obj) -> str:
        """Получить преимущество на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_benefit(language)


class QuotaTypeSerializer(serializers.ModelSerializer):
    """Сериализатор для типов квот"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    requirements = QuotaRequirementSerializer(many=True, read_only=True)
    benefits = QuotaBenefitSerializer(many=True, read_only=True)

    class Meta:
        model = QuotaType
        fields = [
            "id",
            "type",
            "title",
            "description",
            "icon",
            "spots",
            "deadline",
            "color",
            "order",
            "requirements",
            "benefits",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        """Получить название на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class QuotaStatsSerializer(serializers.ModelSerializer):
    """Сериализатор для статистики квот"""

    label = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = QuotaStats
        fields = ["id", "stat_type", "number", "label", "description", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_label(self, obj) -> str:
        """Получить подпись на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_label(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class AdditionalSupportSerializer(serializers.ModelSerializer):
    """Сериализатор для дополнительной поддержки"""

    support = serializers.SerializerMethodField()

    class Meta:
        model = AdditionalSupport
        fields = ["id", "support", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_support(self, obj) -> str:
        """Получить поддержку на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_support(language)


class ProcessStepSerializer(serializers.ModelSerializer):
    """Сериализатор для шагов процесса"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = ProcessStep
        fields = ["id", "step_number", "title", "description", "color_scheme"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        """Получить название на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class BachelorQuotasDataSerializer(serializers.Serializer):
    """Комплексный сериализатор для всех данных страницы квот"""

    quotas = QuotaTypeSerializer(many=True)
    quota_stats = QuotaStatsSerializer(many=True)
    additional_support = AdditionalSupportSerializer(many=True)
    process_steps = ProcessStepSerializer(many=True)

    def to_representation(self, instance):
        """Формируем структуру данных для фронтенда"""
        language = self.context.get("language", "ru")

        # Получаем активные данные
        quotas = (
            QuotaType.objects.filter(is_active=True)
            .prefetch_related("requirements", "benefits")
            .order_by("order", "type")
        )

        quota_stats = QuotaStats.objects.filter(is_active=True).order_by("order")
        additional_support = AdditionalSupport.objects.filter(is_active=True).order_by(
            "order"
        )
        process_steps = ProcessStep.objects.filter(is_active=True).order_by(
            "step_number"
        )

        return {
            "quotas": QuotaTypeSerializer(
                quotas, many=True, context={"language": language}
            ).data,
            "quota_stats": QuotaStatsSerializer(
                quota_stats, many=True, context={"language": language}
            ).data,
            "additional_support": AdditionalSupportSerializer(
                additional_support, many=True, context={"language": language}
            ).data,
            "process_steps": ProcessStepSerializer(
                process_steps, many=True, context={"language": language}
            ).data,
        }


class AspirantDocumentsSerializer(serializers.ModelSerializer):
    """Сериализатор для документов аспирантуры"""

    document_name = serializers.SerializerMethodField()

    class Meta:
        model = AspirantDocuments
        fields = ["id", "document_name", "order", "file"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_document_name(self, obj) -> str:
        """Получить название документа на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_document_name(language)


class AspirantMainDateSerializer(serializers.ModelSerializer):
    """Сериализатор для основных дат аспирантуры"""

    event_name = serializers.SerializerMethodField()

    class Meta:
        model = AspirantMainDate
        fields = ["id", "event_name", "date", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_event_name(self, obj) -> str:
        """Получить название события на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_event_name(language)


class AspirantProgramsSerializer(serializers.ModelSerializer):
    """Сериализатор для программ аспирантуры"""

    program_name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()

    class Meta:
        model = AspirantPrograms
        fields = ["id", "program_name", "description", "order", "features"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_program_name(self, obj) -> str:
        """Получить название программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_program_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_features(self, obj) -> str:
        """Получить особенности программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_features(language)


class AspirantRequirementsSerializer(serializers.ModelSerializer):
    """Сериализатор для требований аспирантуры"""

    description = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = AspirantRequirements
        fields = ["id", "description", "order", "title"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        """Получить название на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_title(language)


class AspirantDocumentsSerializer(serializers.ModelSerializer):
    """Сериализатор для документов аспирантуры"""

    document_name = serializers.SerializerMethodField()

    class Meta:
        model = AspirantDocuments
        fields = ["id", "document_name", "order", "file"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_document_name(self, obj) -> str:
        """Получить название документа на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_document_name(language)


class MasterDocumentsSerializer(serializers.ModelSerializer):
    """Сериализатор для документов магистратуры"""

    document_name = serializers.SerializerMethodField()

    class Meta:
        model = MasterDocuments
        fields = ["id", "document_name", "order", "file"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_document_name(self, obj) -> str:
        """Получить название документа на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_document_name(language)


class MasterRequirementsSerializer(serializers.ModelSerializer):
    """Сериализатор для требований магистратуры"""

    description = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = MasterRequirements
        fields = ["id", "description", "order", "title"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        """Получить название на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_title(language)


class MasterMainDateSerializer(serializers.ModelSerializer):
    """Сериализатор для основных дат магистратуры"""

    event_name = serializers.SerializerMethodField()

    class Meta:
        model = MasterMainDate
        fields = ["id", "event_name", "date", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_event_name(self, obj) -> str:
        """Получить название события на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_event_name(language)


class MasterProgramsSerializer(serializers.ModelSerializer):
    """Сериализатор для программ магистратуры"""

    program_name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()

    class Meta:
        model = MasterPrograms
        fields = ["id", "program_name", "description", "order", "features"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_program_name(self, obj) -> str:
        """Получить название программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_program_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_features(self, obj) -> str:
        """Получить особенности программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_features(language)


class DoctorAdmissionStepsSerializer(serializers.Serializer):
    """Сериализатор для шагов приема в докторантуру"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    deadline = serializers.SerializerMethodField()
    requirement = serializers.SerializerMethodField()

    class Meta:
        model = DoctorAdmissionSteps
        fields = [
            "id",
            "order",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        """Получить название шага на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание шага на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_deadline(self, obj) -> str:
        """Получить крайний срок шага на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_deadline(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_requirement(self, obj) -> str:
        """Получить требования шага на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_requirement(language)


class DoctorStatisticsSerializer(serializers.ModelSerializer):
    """Сериализатор для статистики докторантуры"""

    description = serializers.SerializerMethodField()

    class Meta:
        model = DoctorStatistics
        fields = [
            "titleInt",
            "description",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class DoctorProgramsShortSerializer(serializers.ModelSerializer):
    """Сериализатор для программ докторантуры"""

    program_name = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()

    class Meta:
        model = DoctorPrograms
        fields = ["id", "program_name", "duration", "features", "short_description"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_program_name(self, obj) -> str:
        """Получить название программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_program_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_features(self, obj) -> str:
        """Получить особенности программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_features(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_short_description(self, obj) -> str:
        """Получить краткое описание программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_short_description(language)


class DoctorProgramsFullSerializer(serializers.ModelSerializer):
    """Сериализатор для подробной информации о программе докторантуры"""

    program_name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()

    class Meta:
        model = DoctorPrograms
        fields = [
            "id",
            "program_name",
            "description",
            "features",
            "duration",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_program_name(self, obj) -> str:
        """Получить название программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_program_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_features(self, obj) -> str:
        """Получить особенности программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_features(language)


class DoctorSoonEventsSerializer(serializers.Serializer):
    """Сериализатор для предстоящих событий докторантуры"""

    event = serializers.SerializerMethodField()

    class Meta:
        model = DoctorSoonEvents
        fields = ["event", "date"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_event(self, obj) -> str:
        """Получить событие на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_event(language)


class CollegeSoonEventsSerializer(serializers.Serializer):
    """Сериализатор для предстоящих событий колледжа"""

    event = serializers.SerializerMethodField()

    class Meta:
        model = CollegeSoonEvents
        fields = ["event", "date"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_event(self, obj) -> str:
        """Получить событие на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_event(language)


class CollegeSoonEventsSerializer(serializers.Serializer):
    """Сериализатор для предстоящих событий колледжа"""

    event = serializers.SerializerMethodField()

    class Meta:
        model = CollegeSoonEvents
        fields = ["event", "date"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_event(self, obj) -> str:
        """Получить событие на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_event(language)


class CollegeProgramsFullSerializer(serializers.ModelSerializer):
    """Сериализатор для подробной информации о программе колледжа"""

    program_name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()

    class Meta:
        model = CollegePrograms
        fields = [
            "id",
            "program_name",
            "description",
            "features",
            "duration",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_program_name(self, obj) -> str:
        """Получить название программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_program_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_features(self, obj) -> str:
        """Получить особенности программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_features(language)


class CollegeProgramsShortSerializer(serializers.ModelSerializer):
    """Сериализатор для программ колледжа"""

    program_name = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()

    class Meta:
        model = CollegePrograms
        fields = ["id", "program_name", "duration", "features", "short_description"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_program_name(self, obj) -> str:
        """Получить название программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_program_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_features(self, obj) -> str:
        """Получить особенности программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_features(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_short_description(self, obj) -> str:
        """Получить краткое описание программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_short_description(language)


class CollegeAdmissionStepsSerializer(serializers.Serializer):
    """Сериализатор для шагов приема в колледж"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()

    class Meta:
        model = CollegeAdmissionSteps
        fields = ["id", "order", "title", "description", "duration"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        """Получить название шага на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание шага на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_duration(self, obj) -> str:
        """Получить длительность шага на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_duration(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_requirement(self, obj) -> str:
        """Получить требования шага на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_requirement(language)


class CollegeAdmissionRequirementsSerializer(serializers.Serializer):
    """Сериализатор для требований колледжа"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = CollegeAdmissionRequirements
        fields = ["id", "title", "description"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        """Получить название требования на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание требования на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class CollegeStatisticsSerializer(serializers.ModelSerializer):
    """Сериализатор для статистики колледжа"""

    description = serializers.SerializerMethodField()

    class Meta:
        model = CollegeStatistics
        fields = [
            "titleInt",
            "description",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class BachelorProgramsSerializer(serializers.ModelSerializer):
    """Сериализатор для программ бакалавриата"""

    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    mainDiscipline = serializers.SerializerMethodField()
    CareerPerspectives = serializers.SerializerMethodField()

    class Meta:
        model = BachelorProgram
        fields = [
            "id",
            "name",
            "description",
            "duration",
            "Offline",
            "emoji",
            "mainDiscipline",
            "CareerPerspectives",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        """Получить название программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    @extend_schema_field(OpenApiTypes.OBJECT)
    def get_mainDiscipline(self, obj):
        """Получить основную дисциплину программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_mainDiscipline(language)

    @extend_schema_field(OpenApiTypes.OBJECT)
    def get_CareerPerspectives(self, obj):
        """Получить карьерные перспективы программы на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_CareerPerspectives(language)
