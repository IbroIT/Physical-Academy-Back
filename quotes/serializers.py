from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from .models import Quote, QuoteTranslation

class QuoteTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteTranslation
        fields = ['language', 'text', 'author', 'author_title']

class QuoteSerializer(serializers.ModelSerializer):
    translations = QuoteTranslationSerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Quote
        fields = ['id', 'image_url', 'is_active', 'order', 'created_at', 'translations']

    @extend_schema_field(OpenApiTypes.STR)
    def get_image_url(self, obj):
        if not obj.image:
            return None
        try:
            return obj.image.url
        except Exception:
            return str(obj.image)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        language = request.query_params.get('lang', 'ru') if request else 'ru'
        
        # Находим перевод для запрошенного языка
        translation = instance.translations.filter(language=language).first()
        
        if translation:
            data['text'] = translation.text
            data['author'] = translation.author
            data['author_title'] = translation.author_title
        else:
            # Fallback на русский язык
            ru_translation = instance.translations.filter(language='ru').first()
            if ru_translation:
                data['text'] = ru_translation.text
                data['author'] = ru_translation.author
                data['author_title'] = ru_translation.author_title
            else:
                # Если нет даже русского перевода, берем первый доступный
                first_translation = instance.translations.first()
                if first_translation:
                    data['text'] = first_translation.text
                    data['author'] = first_translation.author
                    data['author_title'] = first_translation.author_title
        
        return data