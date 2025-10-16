from rest_framework import serializers
from .models_disabilities import (
    DisabilitySupportService,
    DisabilityContactPerson,
    DisabilityResource,
    DisabilityEmergencyContact,
)


class DisabilitySupportServiceSerializer(serializers.ModelSerializer):
    """Serializer for disability support services with language selection"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()

    class Meta:
        model = DisabilitySupportService
        fields = ["id", "icon", "title", "description", "features"]

    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"title_{language}")

    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"description_{language}")

    def get_features(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_features_list(language)


class DisabilityContactPersonSerializer(serializers.ModelSerializer):
    """Serializer for disability contact persons with language selection"""

    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    hours = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        model = DisabilityContactPerson
        fields = [
            "id",
            "icon",
            "name",
            "position",
            "phone",
            "email",
            "hours",
            "location",
        ]

    def get_name(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"name_{language}")

    def get_position(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"position_{language}")

    def get_hours(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"hours_{language}", None)

    def get_location(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"location_{language}", None)


class DisabilityResourceSerializer(serializers.ModelSerializer):
    """Serializer for disability resources with language selection"""

    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    format = serializers.SerializerMethodField()

    class Meta:
        model = DisabilityResource
        fields = ["id", "icon", "name", "description", "url", "type", "format"]

    def get_name(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"name_{language}")

    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"description_{language}")

    def get_type(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"type_{language}")

    def get_format(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"format_{language}")


class DisabilityEmergencyContactSerializer(serializers.ModelSerializer):
    """Serializer for disability emergency contacts with language selection"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    phoneLink = serializers.SerializerMethodField()

    class Meta:
        model = DisabilityEmergencyContact
        # Keep snake_case 'phone_link' for backward compatibility and add camelCase 'phoneLink'
        fields = ["id", "title", "description", "phone", "phone_link", "phoneLink"]

    def get_title(self, obj):
        language = self.context.get("language", "ru")
        # Check if obj is a QuerySet and handle it appropriately
        if hasattr(obj, "all") and callable(obj.all):
            # This is a QuerySet - this shouldn't normally happen with proper 'many=True'
            # But we'll handle it by returning the first item's title
            first_item = obj.first()
            return getattr(first_item, f"title_{language}") if first_item else ""
        # Normal case - obj is a model instance
        return getattr(obj, f"title_{language}", "")

    def get_description(self, obj):
        language = self.context.get("language", "ru")
        # Check if obj is a QuerySet and handle it appropriately
        if hasattr(obj, "all") and callable(obj.all):
            # This is a QuerySet - this shouldn't normally happen with proper 'many=True'
            # But we'll handle it by returning the first item's description
            first_item = obj.first()
            return getattr(first_item, f"description_{language}") if first_item else ""
        # Normal case - obj is a model instance
        return getattr(obj, f"description_{language}", "")

    def get_phoneLink(self, obj):
        # Provide camelCase alias for phone_link to match frontend expectation
        # obj may be a QuerySet in some edge cases handled above; normalize
        if hasattr(obj, "all") and callable(obj.all):
            first_item = obj.first()
            return getattr(first_item, "phone_link") if first_item else ""
        return getattr(obj, "phone_link", "")


class DisabilitiesPageDataSerializer(serializers.Serializer):
    """Combined serializer for the entire disabilities page data"""

    support_services = DisabilitySupportServiceSerializer(many=True, read_only=True)
    contacts = DisabilityContactPersonSerializer(many=True, read_only=True)
    resources = DisabilityResourceSerializer(many=True, read_only=True)
    emergency = DisabilityEmergencyContactSerializer(read_only=True)
