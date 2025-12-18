from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
import cloudinary
from .models import (
    TabCategory,
    Card,
    TimelineEvent,
    AboutFaculty,
    Management,
    Specialization,
    Department,
    DepartmentStaff,
)


class CardSerializer(serializers.ModelSerializer):
    """Сериализатор для карточек"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = ["id", "title", "description", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class TimelineEventSerializer(serializers.ModelSerializer):
    """Сериализатор для событий истории"""

    image = serializers.SerializerMethodField()
    event = serializers.SerializerMethodField()

    class Meta:
        model = TimelineEvent
        fields = ["id", "image", "event", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_event(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_event(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_image(self, obj) -> str:
        if not obj.image:
            return None

        try:
            return obj.image.url
        except Exception:
            return str(obj.image)


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


class FacultyDataSerializer(serializers.Serializer):
    """Общий сериализатор для всех данных факультета"""

    tabs = TabCategorySerializer(many=True)


class AboutFacultySerializer(serializers.ModelSerializer):
    """Сериализатор для текста 'О факультете'"""

    text = serializers.SerializerMethodField()

    class Meta:
        model = AboutFaculty
        fields = ["id", "text", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_text(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_text(language)


class ManagementSerializer(serializers.ModelSerializer):
    """Сериализатор для руководства факультета"""

    name = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    resume = serializers.SerializerMethodField()

    class Meta:
        model = Management
        fields = ["id", "name", "role", "photo", "phone", "email", "resume", "order"]

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

    @extend_schema_field(OpenApiTypes.STR)
    def get_resume(self, obj) -> str | None:
        resume = getattr(obj, "resume", None)
        if not resume:
            return None
        try:
            url = resume.url
            # Для raw файлов Cloudinary генерируем signed URL для безопасного доступа
            if 'cloudinary.com' in url and '/raw/upload/' in url:
                # Извлекаем public_id из URL
                parts = url.split('/upload/')
                if len(parts) > 1:
                    public_id = parts[1].split('.')[0]  # Убираем расширение
                    # Генерируем signed URL с длительным сроком действия
                    url = cloudinary.utils.cloudinary_url(
                        public_id,
                        resource_type="raw",
                        type="upload",
                        sign_url=True,
                        secure=True,
                    )[0]
            return url
        except Exception as e:
            # В случае ошибки возвращаем оригинальный URL
            try:
                return resume.url
            except:
                return str(resume)


class SpecializationSerializer(serializers.ModelSerializer):
    """Сериализатор для специализаций факультета"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Specialization
        fields = ["id", "title", "description", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class DepartmentStaffSerializer(serializers.ModelSerializer):
    """Сериализатор для сотрудников кафедры"""

    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    resume = serializers.SerializerMethodField()

    class Meta:
        model = DepartmentStaff
        fields = ["id", "name", "position", "resume", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_position(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_position(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_resume(self, obj) -> str | None:
        resume = getattr(obj, "resume", None)
        if not resume:
            return None
        try:
            url = resume.url
            # Для raw файлов Cloudinary генерируем signed URL для безопасного доступа
            if 'cloudinary.com' in url and '/raw/upload/' in url:
                # Извлекаем public_id из URL
                parts = url.split('/upload/')
                if len(parts) > 1:
                    public_id = parts[1].split('.')[0]  # Убираем расширение
                    # Генерируем signed URL с длительным сроком действия
                    url = cloudinary.utils.cloudinary_url(
                        public_id,
                        resource_type="raw",
                        type="upload",
                        sign_url=True,
                        secure=True,
                    )[0]
            return url
        except Exception as e:
            # В случае ошибки возвращаем оригинальный URL
            try:
                return resume.url
            except:
                return str(resume)


class DepartmentSerializer(serializers.ModelSerializer):
    """Сериализатор для кафедр факультета"""

    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    staff = DepartmentStaffSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ["id", "name", "description", "staff", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_description(language)
