from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from .models_scholarship_visa import (
    ScholarshipProgram,
    ScholarshipRequiredDocument,
    VisaSupportService,
    VisaSupportContact,
)


class ScholarshipRequiredDocumentSerializer(serializers.ModelSerializer):
    """Сериализатор для требуемых документов для стипендии"""

    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = ScholarshipRequiredDocument
        fields = ["id", "name", "description", "is_required", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_field("name", lang)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_field("description", lang)


class ScholarshipProgramSerializer(serializers.ModelSerializer):
    """Сериализатор для стипендиальных программ"""

    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    eligibility_criteria = serializers.SerializerMethodField()
    required_documents = ScholarshipRequiredDocumentSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = ScholarshipProgram
        fields = [
            "id",
            "name",
            "description",
            "eligibility_criteria",
            "amount",
            "currency",
            "application_deadline",
            "application_link",
            "contact_email",
            "contact_phone",
            "required_documents",
            "is_active",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_field("name", lang)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_field("description", lang)

    @extend_schema_field(OpenApiTypes.STR)
    def get_eligibility_criteria(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_field("eligibility_criteria", lang)


class VisaSupportContactSerializer(serializers.ModelSerializer):
    """Сериализатор для контактов по визовой поддержке"""

    full_name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    office_location = serializers.SerializerMethodField()
    office_hours = serializers.SerializerMethodField()

    class Meta:
        model = VisaSupportContact
        fields = [
            "id",
            "full_name",
            "position",
            "email",
            "phone",
            "photo",
            "office_location",
            "office_hours",
            "order",
            "is_active",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_full_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_field("full_name", lang)

    @extend_schema_field(OpenApiTypes.STR)
    def get_position(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_field("position", lang)

    @extend_schema_field(OpenApiTypes.STR)
    def get_office_location(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_field("office_location", lang)

    @extend_schema_field(OpenApiTypes.STR)
    def get_office_hours(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_field("office_hours", lang)


class VisaSupportServiceSerializer(serializers.ModelSerializer):
    """Сериализатор для сервисов визовой поддержки"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = VisaSupportService
        fields = [
            "id",
            "title",
            "description",
            "is_featured",
            "icon",
            "order",
            "is_active",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_field("title", lang)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_field("description", lang)


class ScholarshipPageDataSerializer(serializers.Serializer):
    """Сериализатор для полной страницы стипендий"""

    scholarships = ScholarshipProgramSerializer(many=True, read_only=True)
    total_scholarships = serializers.IntegerField()
    active_scholarships = serializers.IntegerField()

    def to_representation(self, instance):
        lang = self.context.get("language", "ru")

        # Получаем все активные стипендии
        scholarships = ScholarshipProgram.objects.filter(is_active=True).order_by(
            "name_ru"
        )

        # Статистика
        total_scholarships = ScholarshipProgram.objects.count()
        active_scholarships = scholarships.count()

        # Сериализуем данные о стипендиях
        scholarship_serializer = ScholarshipProgramSerializer(
            scholarships, many=True, context={"language": lang}
        )

        return {
            "scholarships": scholarship_serializer.data,
            "total_scholarships": total_scholarships,
            "active_scholarships": active_scholarships,
        }


class VisaSupportPageDataSerializer(serializers.Serializer):
    """Сериализатор для полной страницы визовой поддержки"""

    services = VisaSupportServiceSerializer(many=True, read_only=True)
    contacts = VisaSupportContactSerializer(many=True, read_only=True)
    featured_services = VisaSupportServiceSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        lang = self.context.get("language", "ru")

        # Получаем все активные сервисы
        services = VisaSupportService.objects.filter(is_active=True).order_by("order")
        featured_services = services.filter(is_featured=True)

        # Получаем контакты
        contacts = VisaSupportContact.objects.filter(is_active=True).order_by("order")

        # Сериализуем данные
        services_serializer = VisaSupportServiceSerializer(
            services, many=True, context={"language": lang}
        )

        featured_serializer = VisaSupportServiceSerializer(
            featured_services, many=True, context={"language": lang}
        )

        contacts_serializer = VisaSupportContactSerializer(
            contacts, many=True, context={"language": lang}
        )

        return {
            "services": services_serializer.data,
            "contacts": contacts_serializer.data,
            "featured_services": featured_serializer.data,
        }
