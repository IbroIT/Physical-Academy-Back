from rest_framework import serializers
from .models import Fact, FactTranslation

class FactTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactTranslation
        fields = ['language', 'label']

class FactSerializer(serializers.ModelSerializer):
    translations = FactTranslationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Fact
        fields = [
            'id', 'end_value', 'icon', 'duration', 'delay', 
            'color', 'is_active', 'order', 'created_at', 'translations'
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        language = request.query_params.get('lang', 'ru') if request else 'ru'
        
        # Находим перевод для запрошенного языка
        translation = instance.translations.filter(language=language).first()
        
        if translation:
            data['label'] = translation.label
        else:
            # Fallback на русский язык
            ru_translation = instance.translations.filter(language='ru').first()
            if ru_translation:
                data['label'] = ru_translation.label
            else:
                # Если нет даже русского перевода, берем первый доступный
                first_translation = instance.translations.first()
                if first_translation:
                    data['label'] = first_translation.label
        
        return data