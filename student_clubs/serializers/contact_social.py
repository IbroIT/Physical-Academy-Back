from rest_framework import serializers
from ..models.contact_social import (
    StudentContactInfo,
    SocialNetworkAccount,
    SocialCommunity,
)


class StudentContactInfoSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    contact_name = serializers.SerializerMethodField()
    office_location = serializers.SerializerMethodField()
    office_hours = serializers.SerializerMethodField()

    class Meta:
        model = StudentContactInfo
        fields = [
            "id",
            "title",
            "description",
            "contact_name",
            "email",
            "phone",
            "office_location",
            "office_hours",
            "is_featured",
            "photo",
            "order",
            "is_active",
        ]

    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_field("title", language)

    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_field("description", language)

    def get_contact_name(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_field("contact_name", language)

    def get_office_location(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_field("office_location", language)

    def get_office_hours(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_field("office_hours", language)


class SocialNetworkAccountSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    network_display = serializers.CharField(
        source="get_network_display", read_only=True
    )

    class Meta:
        model = SocialNetworkAccount
        fields = [
            "id",
            "network",
            "network_display",
            "name",
            "description",
            "url",
            "username",
            "icon",
            "color_hex",
            "is_featured",
            "is_official",
            "order",
            "is_active",
        ]

    def get_name(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_field("name", language)

    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_field("description", language)


class SocialCommunitySerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    network_display = serializers.CharField(
        source="get_network_display", read_only=True
    )

    class Meta:
        model = SocialCommunity
        fields = [
            "id",
            "title",
            "description",
            "members_count",
            "posts_count",
            "network",
            "network_display",
            "url",
            "banner_image",
            "is_featured",
            "is_verified",
            "order",
            "is_active",
        ]

    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_field("title", language)

    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_field("description", language)
