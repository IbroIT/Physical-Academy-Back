from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from .models import  DepartmentInfo, Management, TabCategory




class ManagementSerializer(serializers.ModelSerializer):
    """Сериализатор для руководства факультета"""

    name = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

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

    class Meta:
        model = TabCategory
        fields = ["id", "name"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)



class DepartmentCategoryDetailSerializer(serializers.ModelSerializer):
    """Детальный сериализатор категории с полной информацией"""

    name = serializers.SerializerMethodField()
    info = serializers.SerializerMethodField()
    management = serializers.SerializerMethodField()

    class Meta:
        model = TabCategory
        fields = ["id", "name", "color", "order", "info", "management"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(DepartmentInfoSerializer)
    def get_info(self, obj):
        try:
            info = obj.info
            if info.is_active:
                return DepartmentInfoSerializer(info, context=self.context).data
        except Exception:
            return None
        return None

    @extend_schema_field(ManagementSerializer(many=True))
    def get_management(self, obj):
        items = obj.management.filter(is_active=True).order_by("order")
        return ManagementSerializer(items, many=True, context=self.context).data
