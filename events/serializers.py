from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    # Динамические поля для текущего языка
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    full_description = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    audience = serializers.SerializerMethodField()
    format = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    organizer = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'full_description',
            'category',
            'department',
            'image',
            'date',
            'time',
            'location',
            'audience',
            'format',
            'duration',
            'organizer',
            'is_active',
            'is_featured',
            'order',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def get_title(self, obj):
        request = self.context.get('request')
        language = getattr(request, 'LANGUAGE_CODE', 'ru') if request else 'ru'
        return obj.get_title(language)

    def get_description(self, obj):
        request = self.context.get('request')
        language = getattr(request, 'LANGUAGE_CODE', 'ru') if request else 'ru'
        return obj.get_description(language)

    def get_full_description(self, obj):
        request = self.context.get('request')
        language = getattr(request, 'LANGUAGE_CODE', 'ru') if request else 'ru'
        full_desc = obj.get_full_description(language)
        return full_desc if full_desc else obj.get_description(language)

    def get_location(self, obj):
        request = self.context.get('request')
        language = getattr(request, 'LANGUAGE_CODE', 'ru') if request else 'ru'
        return obj.get_location(language)

    def get_audience(self, obj):
        request = self.context.get('request')
        language = getattr(request, 'LANGUAGE_CODE', 'ru') if request else 'ru'
        return obj.get_audience(language)

    def get_format(self, obj):
        request = self.context.get('request')
        language = getattr(request, 'LANGUAGE_CODE', 'ru') if request else 'ru'
        return obj.get_format(language)

    def get_duration(self, obj):
        request = self.context.get('request')
        language = getattr(request, 'LANGUAGE_CODE', 'ru') if request else 'ru'
        return obj.get_duration(language)

    def get_organizer(self, obj):
        request = self.context.get('request')
        language = getattr(request, 'LANGUAGE_CODE', 'ru') if request else 'ru'
        
        organizer_name = obj.get_organizer_name(language)
        organizer_contact = obj.get_organizer_contact(language)
        
        if organizer_name or organizer_contact:
            return {
                'name': organizer_name,
                'contact': organizer_contact
            }
        return None

class EventListSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'category',
            'department',
            'image',
            'date',
            'time',
            'location',
            'is_featured',
            'order'
        ]

    def get_title(self, obj):
        request = self.context.get('request')
        language = getattr(request, 'LANGUAGE_CODE', 'ru') if request else 'ru'
        return obj.get_title(language)

    def get_description(self, obj):
        request = self.context.get('request')
        language = getattr(request, 'LANGUAGE_CODE', 'ru') if request else 'ru'
        return obj.get_description(language)

    def get_location(self, obj):
        request = self.context.get('request')
        language = getattr(request, 'LANGUAGE_CODE', 'ru') if request else 'ru'
        return obj.get_location(language)