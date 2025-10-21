from rest_framework import serializers
from .models_disabilities import DisabilityPage
from .serializers_base import LanguageAwareSerializer


class DisabilityPageSerializer(LanguageAwareSerializer):
    """Serializer for disability pages with multilingual support"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = DisabilityPage
        fields = ["id", "title", "description"]

    def get_title(self, obj):
        """Get title in requested language"""
        return self.get_language_field(obj, "title", "")

    def get_description(self, obj):
        """Get description in requested language"""
        return self.get_language_field(obj, "description", "")
