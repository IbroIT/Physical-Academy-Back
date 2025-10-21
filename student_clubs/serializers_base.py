from rest_framework import serializers


class LanguageAwareSerializer(serializers.ModelSerializer):
    """
    Base serializer for models with language-specific fields.
    This serializer automatically handles language selection based on the request context.
    """

    def get_language(self):
        """Get language from context or use default"""
        # Try to get language from serializer context
        lang = self.context.get("language", "ru")
        # Validate language
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"
        return lang

    def get_language_field(self, obj, field_name, default=None):
        """
        Generic method to get a language-specific field value.

        Args:
            obj: The model instance
            field_name: The base field name without language suffix (e.g. 'title')
            default: Default value if field doesn't exist

        Returns:
            The value of the field in the current language
        """
        language = self.get_language()
        return getattr(obj, f"{field_name}_{language}", default)
