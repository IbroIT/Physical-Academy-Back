from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from .models import DepartmentCategory, DepartmentInfo


class DepartmentInfoSerializer(serializers.ModelSerializer):
    """Сериализатор для информации о кафедре"""

    content = serializers.SerializerMethodField()

    class Meta:
        model = DepartmentInfo
        fields = ["id", "info_type", "content", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_content(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_content(language)


class DepartmentCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категории кафедры"""

    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()

    class Meta:
        model = DepartmentCategory
        fields = ["id", "key", "name", "color", "description", "features", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        # Получаем первое описание
        description_item = obj.info_items.filter(
            info_type="description", is_active=True
        ).first()
        return description_item.get_content(language) if description_item else ""

    @extend_schema_field(OpenApiTypes.OBJECT)
    def get_features(self, obj) -> list:
        language = self.context.get("language", "ru")
        # Получаем все активные особенности
        features = obj.info_items.filter(info_type="feature", is_active=True).order_by(
            "order"
        )
        return [feature.get_content(language) for feature in features]


class DepartmentCategoryDetailSerializer(serializers.ModelSerializer):
    """Детальный сериализатор категории с полной информацией"""

    name = serializers.SerializerMethodField()
    info_items = DepartmentInfoSerializer(many=True, read_only=True)

    class Meta:
        model = DepartmentCategory
        fields = ["id", "key", "name", "color", "order", "info_items"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    def to_representation(self, instance):
        language = self.context.get("language", "ru")
        self.fields["info_items"].context.update({"language": language})
        return super().to_representation(instance)
