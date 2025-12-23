from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from .models import  MasterDepartmentInfo, MasterManagement, MasterTabCategory, PhdDepartmentInfo, PhdManagement, PhdTabCategory, CollegeDepartmentInfo, CollegeManagement, CollegeTabCategory



class CollegeManagementSerializer(serializers.ModelSerializer):
    """Сериализатор для руководства факультета"""

    name = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = CollegeManagement
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


class CollegeDepartmentInfoSerializer(serializers.ModelSerializer):
    """Сериализатор для описания кафедры"""

    description = serializers.SerializerMethodField()

    class Meta:
        model = CollegeDepartmentInfo
        fields = ["id", "description"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class CollegeDepartmentCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категории кафедры"""

    name = serializers.SerializerMethodField()

    class Meta:
        model = CollegeTabCategory
        fields = ["id", "name"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)



class CollegeDepartmentCategoryDetailSerializer(serializers.ModelSerializer):
    """Детальный сериализатор категории с полной информацией"""

    name = serializers.SerializerMethodField()
    info = serializers.SerializerMethodField()
    management = serializers.SerializerMethodField()

    class Meta:
        model = CollegeTabCategory
        fields = ["id", "name", "color", "order", "info", "management"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(CollegeDepartmentInfoSerializer)
    def get_info(self, obj):
        try:
            info = obj.info
            if info.is_active:
                return CollegeDepartmentInfoSerializer(info, context=self.context).data
        except Exception:
            return None
        return None

    @extend_schema_field(CollegeManagementSerializer(many=True))
    def get_management(self, obj):
        items = obj.management.filter(is_active=True).order_by("order")
        return CollegeManagementSerializer(items, many=True, context=self.context).data


class PhdManagementSerializer(serializers.ModelSerializer):
    """Сериализатор для руководства факультета"""

    name = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = PhdManagement
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


class PhdDepartmentInfoSerializer(serializers.ModelSerializer):
    """Сериализатор для описания кафедры"""

    description = serializers.SerializerMethodField()

    class Meta:
        model = PhdDepartmentInfo
        fields = ["id", "description"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class PhdDepartmentCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категории кафедры"""

    name = serializers.SerializerMethodField()

    class Meta:
        model = MasterTabCategory
        fields = ["id", "name"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)



class PhdDepartmentCategoryDetailSerializer(serializers.ModelSerializer):
    """Детальный сериализатор категории с полной информацией"""

    name = serializers.SerializerMethodField()
    info = serializers.SerializerMethodField()
    management = serializers.SerializerMethodField()

    class Meta:
        model = PhdTabCategory
        fields = ["id", "name", "color", "order", "info", "management"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(PhdDepartmentInfoSerializer)
    def get_info(self, obj):
        try:
            info = obj.info
            if info.is_active:
                return PhdDepartmentInfoSerializer(info, context=self.context).data
        except Exception:
            return None
        return None

    @extend_schema_field(PhdManagementSerializer(many=True))
    def get_management(self, obj):
        items = obj.management.filter(is_active=True).order_by("order")
        return PhdManagementSerializer(items, many=True, context=self.context).datPhd


class MasterManagementSerializer(serializers.ModelSerializer):
    """Сериализатор для руководства факультета"""

    name = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = MasterManagement
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


class MasterDepartmentInfoSerializer(serializers.ModelSerializer):
    """Сериализатор для описания кафедры"""

    description = serializers.SerializerMethodField()

    class Meta:
        model = MasterDepartmentInfo
        fields = ["id", "description"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class MasterDepartmentCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категории кафедры"""

    name = serializers.SerializerMethodField()

    class Meta:
        model = MasterTabCategory
        fields = ["id", "name"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)



class MasterDepartmentCategoryDetailSerializer(serializers.ModelSerializer):
    """Детальный сериализатор категории с полной информацией"""

    name = serializers.SerializerMethodField()
    info = serializers.SerializerMethodField()
    management = serializers.SerializerMethodField()

    class Meta:
        model = MasterTabCategory
        fields = ["id", "name", "color", "order", "info", "management"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(MasterDepartmentInfoSerializer)
    def get_info(self, obj):
        try:
            info = obj.info
            if info.is_active:
                return MasterDepartmentInfoSerializer(info, context=self.context).data
        except Exception:
            return None
        return None

    @extend_schema_field(MasterManagementSerializer(many=True))
    def get_management(self, obj):
        items = obj.management.filter(is_active=True).order_by("order")
        return MasterManagementSerializer(items, many=True, context=self.context).data
