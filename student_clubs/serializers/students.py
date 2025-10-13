from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from ..models import StudentProfile, ClubMembership, Club
from .clubs import ClubListSerializer


class StudentProfileSerializer(serializers.ModelSerializer):
    """Сериализатор профиля студента"""

    full_name = serializers.SerializerMethodField()
    faculty = serializers.SerializerMethodField()
    major = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()

    class Meta:
        model = StudentProfile
        fields = [
            "id",
            "full_name",
            "email",
            "phone",
            "faculty",
            "year_of_study",
            "major",
            "bio",
            "interests",
            "photo",
            "is_active",
            "created_at",
            "updated_at",
            # Языковые поля для админки
            "full_name_ru",
            "full_name_en",
            "full_name_kg",
            "faculty_ru",
            "faculty_en",
            "faculty_kg",
            "major_ru",
            "major_en",
            "major_kg",
            "bio_ru",
            "bio_en",
            "bio_kg",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_full_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("full_name", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_faculty(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("faculty", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_major(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("major", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_bio(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("bio", language)


class ClubMembershipSerializer(serializers.ModelSerializer):
    """Сериализатор для членства в клубе"""

    student = StudentProfileSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=StudentProfile.objects.all(), write_only=True, source="student"
    )
    club = ClubListSerializer(read_only=True)
    club_id = serializers.PrimaryKeyRelatedField(
        queryset=StudentProfile.objects.all(), write_only=True, source="club"
    )
    role = serializers.SerializerMethodField()

    class Meta:
        model = ClubMembership
        fields = [
            "id",
            "student",
            "student_id",
            "club",
            "club_id",
            "status",
            "joined_at",
            "updated_at",
            "motivation_text",
            "role",
            "role_ru",
            "role_en",
            "role_kg",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_role(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("role", language)


class StudentProfileCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания профиля студента"""

    class Meta:
        model = StudentProfile
        fields = [
            "full_name_ru",
            "full_name_en",
            "full_name_kg",
            "email",
            "phone",
            "faculty_ru",
            "faculty_en",
            "faculty_kg",
            "year_of_study",
            "major_ru",
            "major_en",
            "major_kg",
            "bio_ru",
            "bio_en",
            "bio_kg",
            "interests",
            "photo",
        ]


class StudentProfileListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка профилей студентов"""

    full_name = serializers.SerializerMethodField()
    faculty = serializers.SerializerMethodField()

    class Meta:
        model = StudentProfile
        fields = [
            "id",
            "full_name",
            "email",
            "faculty",
            "year_of_study",
            "photo",
            "is_active",
            "created_at",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_full_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("full_name", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_faculty(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("faculty", language)


class ClubMembershipCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания членства в клубе"""

    class Meta:
        model = ClubMembership
        fields = [
            "student",
            "club",
            "status",
            "motivation_text",
            "role_ru",
            "role_en",
            "role_kg",
        ]


class StudentClubsSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения клубов с информацией о статусе членства студента"""

    name = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    membership = serializers.SerializerMethodField()

    class Meta:
        model = Club
        fields = [
            "id",
            "name",
            "icon",
            "short_description",
            "category",
            "category_name",
            "membership",
            "members_count",
            "status",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_field("name", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_short_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_field("short_description", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_category_name(self, obj):
        language = self.context.get("language", "ru")
        return obj.category.get_name(language)

    @extend_schema_field(OpenApiTypes.OBJECT)
    def get_membership(self, obj):
        # Получаем словарь членств из контекста
        memberships = self.context.get("memberships", {})
        membership = memberships.get(obj.id)

        if not membership:
            return None

        return {
            "id": membership.id,
            "status": membership.status,
            "joined_at": membership.joined_at,
            "role": membership.get_field("role", self.context.get("language", "ru")),
        }
