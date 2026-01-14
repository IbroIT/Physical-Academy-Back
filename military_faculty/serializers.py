from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from .models import (
    TabCategory,
    Card,
    TimelineEvent,
    AboutFaculty,
    Management,
    Specialization,
    Department,
    DepartmentStaff,
    GalleryCard
)
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
        if not obj.resume:
            return None
        request = self.context.get('request')
        if request:
            from django.urls import reverse
            # Возвращаем URL на endpoint для скачивания
            download_url = reverse('pedagogical_faculty:download-resume', 
                                  kwargs={'model_type': 'staff', 'pk': obj.pk})
            return request.build_absolute_uri(download_url)
        return None


class GalleryCardSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    
    class Meta:
        model = GalleryCard
        fields = ["id", "title", "description", "photo"]

    def get_title(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_title(language)
    
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_description(language)
    
    @extend_schema_field(OpenApiTypes.STR)
    def get_photo(self, obj) -> str | None:
        img = getattr(obj, "photo", None)
        if not img:
            return None
        try:
            return img.url
        except Exception:
            return str(img)


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

        # CloudinaryField may be stored as a string or an object; be defensive
        try:
            return obj.image.url
        except Exception:
            return str(obj.image)


class TabCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий/табов"""

    title = serializers.SerializerMethodField()
    icon = serializers.SerializerMethodField()

    class Meta:
        model = TabCategory
        fields = ["id", "key", "title", "icon", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_title(language)
    
    @extend_schema_field(OpenApiTypes.STR)
    def get_icon(self, obj) -> str | None:
        img = getattr(obj, "icon", None)
        if not img:
            return None
        try:
            return img.url
        except Exception:
            return str(img)


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
            return resume.url
        except Exception:
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
