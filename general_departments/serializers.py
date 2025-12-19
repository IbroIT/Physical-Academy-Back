from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from .models import DepartmentCategory, DepartmentInfo, DepartmentFeature, Management, TabCategory


class TabCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий/табов"""

    title = serializers.SerializerMethodField()

    class Meta:
        model = TabCategory
        fields = ["id", "key", "title", "icon", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_title(language)


class ManagementSerializer(serializers.ModelSerializer):
    """Сериализатор для руководства факультета"""

    name = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    resume = serializers.SerializerMethodField()

    class Meta:
        model = Management
        fields = ["id", "name", "role", "photo", "phone", "email", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_role(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_role(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_photo(self, obj) -> str | None:
        img = getattr(obj, "photo", None)
        if not img:
            return None
        try:
            return img.url
        except Exception:
            return str(img)


class DepartmentFeatureSerializer(serializers.ModelSerializer):
    """Сериализатор для особенностей кафедры"""

    feature = serializers.SerializerMethodField()

    class Meta:
        model = DepartmentFeature
        fields = ["id", "feature", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_feature(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_feature(language)


class DepartmentInfoSerializer(serializers.ModelSerializer):
    """Сериализатор для описания кафедры"""

    description = serializers.SerializerMethodField()

    class Meta:
        model = DepartmentInfo
        fields = ["id", "description"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_description(language)


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
        # Получаем описание (OneToOne relation)
        if hasattr(obj, "info") and obj.info.is_active:
            return obj.info.get_description(language)
        return ""

    @extend_schema_field(OpenApiTypes.OBJECT)
    def get_features(self, obj) -> list:
        language = self.context.get("language", "ru")
        # Получаем все активные особенности
        features = obj.features.filter(is_active=True).order_by("order")
        return [feature.get_feature(language) for feature in features]


class DepartmentCategoryDetailSerializer(serializers.ModelSerializer):
    """Детальный сериализатор категории с полной информацией"""

    name = serializers.SerializerMethodField()
    info = DepartmentInfoSerializer(read_only=True)
    features = DepartmentFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = DepartmentCategory
        fields = ["id", "key", "name", "color", "order", "info", "features"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    def to_representation(self, instance):
        language = self.context.get("language", "ru")
        self.fields["info"].context.update({"language": language})
        self.fields["features"].context.update({"language": language})
        return super().to_representation(instance)
