from rest_framework import serializers
from .models import (
    CollegePrograms,
    PhdPrograms,
    FacultyTeachers,
    MasterPrograms,
    Faculty,
    FacultyContacts,
    FacultyStatistics,
    FacultySports,
    FacultyPrograms,
    FacultySpecialization,
    FacultySection,
    FacultySectionItem,
)


class FacultyNamesSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = ["name"]

    def get_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_name(lang)


class MasterProgramsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()

    class Meta:
        model = MasterPrograms
        fields = [
            "id",
            "emoji",
            "name",
            "description",
            "features",
            "duration_years",
            "offline",
            "tuition_fee",
        ]

    def get_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_name(lang)

    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_description(lang)

    def get_features(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_features(lang)


class CollegeProgramsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()

    class Meta:
        model = CollegePrograms
        fields = [
            "id",
            "emoji",
            "name",
            "description",
            "features",
            "duration_years",
            "offline",
            "tuition_fee",
        ]

    def get_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_name(lang)

    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_description(lang)

    def get_features(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_features(lang)


class PhdProgramsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()

    class Meta:
        model = PhdPrograms
        fields = [
            "id",
            "emoji",
            "name",
            "description",
            "features",
            "duration_years",
            "offline",
            "tuition_fee",
        ]

    def get_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_name(lang)

    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_description(lang)

    def get_features(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_features(lang)


class FacultyTeachersSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()

    class Meta:
        model = FacultyTeachers
        fields = [
            "id",
            "photo",
            "full_name",
            "position",
        ]

    def get_full_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_full_name(lang)

    def get_position(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_position(lang)


class FacultyContactsSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = FacultyContacts
        fields = ["id", "title", "value"]

    def get_title(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_title(lang)


class FacultyStatisticsSerializer(serializers.ModelSerializer):
    meaning = serializers.SerializerMethodField()

    class Meta:
        model = FacultyStatistics
        fields = ["id", "meaning", "titleInt"]

    def get_meaning(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_meaning(lang)


class FacultySportsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = FacultySports
        fields = ["id", "emoji", "name", "description"]

    def get_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_name(lang)

    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_description(lang)


class FacultyProgramsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    degree = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = FacultyPrograms
        fields = [
            "id",
            "emoji",
            "name",
            "degree",
            "description",
            "duration_years",
            "offline",
            "tuition_fee",
        ]

    def get_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_name(lang)

    def get_degree(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_degree(lang)

    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_description(lang)


class FacultySpecializationSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()

    class Meta:
        model = FacultySpecialization
        fields = ["id", "name", "description", "features"]

    def get_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_name(lang)

    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_description(lang)

    def get_features(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_features(lang)


class FacultySerializer(serializers.ModelSerializer):
    statistics = FacultyStatisticsSerializer(many=True, read_only=True)
    programs = FacultyProgramsSerializer(many=True, read_only=True)
    specializations = FacultySpecializationSerializer(many=True, read_only=True)
    sports = FacultySportsSerializer(many=True, read_only=True)
    teachers = FacultyTeachersSerializer(many=True, read_only=True)
    contacts = FacultyContactsSerializer(many=True, read_only=True)

    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    mission = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = [
            "name",
            "description",
            "mission",
            "achievements",
            "statistics",
            "programs",
            "specializations",
            "sports",
            "teachers",
            "contacts",
        ]

    def get_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_name(lang)

    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_description(lang)

    def get_mission(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_mission(lang)

    def get_achievements(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_achievements(lang)


# Universal Faculty Page Serializers (для публичных страниц)
class FacultySectionItemSerializer(serializers.ModelSerializer):
    """Serializer for individual items within a section"""

    class Meta:
        model = FacultySectionItem
        fields = ["text_ru", "text_en", "text_kg"]

    def to_representation(self, instance):
        """Return only the localized text string"""
        lang = self.context.get("language", "ru")
        return instance.get_text(lang)


class FacultySectionPublicSerializer(serializers.ModelSerializer):
    """Serializer for sections with localized title and items"""

    section_title = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()

    class Meta:
        model = FacultySection
        fields = ["section_title", "items"]

    def get_section_title(self, obj):
        """Return localized section title"""
        lang = self.context.get("language", "ru")
        return obj.get_title(lang)

    def get_items(self, obj):
        """Return list of localized item strings"""
        lang = self.context.get("language", "ru")
        items = obj.items.all()
        return [item.get_text(lang) for item in items]


class FacultyPublicPageSerializer(serializers.ModelSerializer):
    """Main serializer for faculty public pages with full localization"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    sections = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = ["title", "banner_image", "description", "sections"]

    def get_title(self, obj):
        """Return localized title"""
        lang = self.context.get("language", "ru")
        return obj.get_name(lang)

    def get_description(self, obj):
        """Return localized description"""
        lang = self.context.get("language", "ru")
        return obj.get_description(lang)

    def get_sections(self, obj):
        """Return list of localized sections with items"""
        lang = self.context.get("language", "ru")
        sections = obj.public_sections.all()
        serializer = FacultySectionPublicSerializer(
            sections, many=True, context={"language": lang}
        )
        return serializer.data
