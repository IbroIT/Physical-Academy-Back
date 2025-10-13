from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from .models_students import StudentProfile, ClubMembership

# Updated import path for serializers after reorganization
from .serializers.clubs import ClubListSerializer, ClubCategorySerializer
from .models import Club


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
        queryset=Club.objects.all(), write_only=True, source="club"
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
            # Языковые поля для админки
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


class ClubMembershipCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания членства в клубе"""

    class Meta:
        model = ClubMembership
        fields = [
            "student",
            "club",
            "motivation_text",
        ]


class StudentProfileListSerializer(serializers.ModelSerializer):
    """Сокращенный сериализатор для списка студентов"""

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
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_full_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("full_name", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_faculty(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("faculty", language)


class StudentClubsSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения клубов студента"""

    memberships = serializers.SerializerMethodField()

    class Meta:
        model = StudentProfile
        fields = [
            "id",
            "full_name_ru",
            "email",
            "memberships",
        ]

    @extend_schema_field(OpenApiTypes.OBJECT)
    def get_memberships(self, obj):
        memberships = obj.memberships.all().select_related("club")
        result = []
        language = self.context.get("language", "ru")

        for membership in memberships:
            club = membership.club
            result.append(
                {
                    "id": membership.id,
                    "status": membership.status,
                    "joined_at": membership.joined_at,
                    "club": {
                        "id": club.id,
                        "name": club.get_field("name", language),
                        "icon": club.icon,
                        "category": {
                            "id": club.category.id,
                            "name": club.category.get_name(language),
                        },
                    },
                }
            )

        return result
