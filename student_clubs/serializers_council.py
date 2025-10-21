from rest_framework import serializers
from .models_council import CouncilMember, CouncilInitiative, CouncilEvent, CouncilStats


class CouncilMemberSerializer(serializers.ModelSerializer):
    """Serializer for student council members with language selection"""

    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()
    role_display = serializers.SerializerMethodField()

    class Meta:
        model = CouncilMember
        fields = [
            "id",
            "avatar",
            "name",
            "role",
            "role_display",
            "position",
            "department",
            "email",
            "phone",
            "instagram",
            "linkedin",
            "bio",
            "achievements",
        ]

    def get_name(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"name_{language}")

    def get_position(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"position_{language}")

    def get_department(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"department_{language}")

    def get_bio(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"bio_{language}", None)

    def get_achievements(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"achievements_{language}", None)

    def get_role_display(self, obj):
        return obj.get_role_display()


class CouncilInitiativeSerializer(serializers.ModelSerializer):
    """Serializer for student council initiatives with language selection"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    goals = serializers.SerializerMethodField()
    lead_members = CouncilMemberSerializer(many=True, read_only=True)
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = CouncilInitiative
        fields = [
            "id",
            "icon",
            "title",
            "description",
            "goals",
            "status",
            "status_display",
            "start_date",
            "end_date",
            "lead_members",
        ]

    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"title_{language}")

    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"description_{language}")

    def get_goals(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"goals_{language}", None)

    def get_status_display(self, obj):
        return obj.get_status_display()


class CouncilEventSerializer(serializers.ModelSerializer):
    """Serializer for student council events with language selection"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    initiative = CouncilInitiativeSerializer(read_only=True)
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = CouncilEvent
        fields = [
            "id",
            "icon",
            "title",
            "description",
            "status",
            "status_display",
            "date",
            "location",
            "registration_link",
            "image",
            "initiative",
        ]

    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"title_{language}")

    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"description_{language}")

    def get_location(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"location_{language}")

    def get_status_display(self, obj):
        return obj.get_status_display()


class CouncilStatsSerializer(serializers.ModelSerializer):
    """Serializer for student council statistics with language selection"""

    label = serializers.SerializerMethodField()

    class Meta:
        model = CouncilStats
        fields = ["key", "value", "label"]

    def get_label(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"label_{language}")


class CouncilPageDataSerializer(serializers.Serializer):
    """Combined serializer for the entire council page data"""

    members = CouncilMemberSerializer(many=True, read_only=True)
    initiatives = CouncilInitiativeSerializer(many=True, read_only=True)
    events = CouncilEventSerializer(many=True, read_only=True)
    stats = CouncilStatsSerializer(many=True, read_only=True)
