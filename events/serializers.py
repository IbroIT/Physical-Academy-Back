from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    # Мультиязычные поля - возвращаем все языки
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
        return {
            'ru': obj.title_ru,
            'en': obj.title_en,
            'kg': obj.title_kg  # Используем код kg для кыргызского
        }

    def get_description(self, obj):
        return {
            'ru': obj.description_ru,
            'en': obj.description_en,
            'kg': obj.description_kg
        }

    def get_full_description(self, obj):
        return {
            'ru': obj.full_description_ru or obj.description_ru,
            'en': obj.full_description_en or obj.description_en,
            'kg': obj.full_description_kg or obj.description_kg
        }

    def get_location(self, obj):
        return {
            'ru': obj.location_ru,
            'en': obj.location_en,
            'kg': obj.location_kg
        }

    def get_audience(self, obj):
        return {
            'ru': obj.audience_ru,
            'en': obj.audience_en,
            'kg': obj.audience_kg
        }

    def get_format(self, obj):
        return {
            'ru': obj.format_ru,
            'en': obj.format_en,
            'kg': obj.format_kg
        }

    def get_duration(self, obj):
        return {
            'ru': obj.duration_ru,
            'en': obj.duration_en,
            'kg': obj.duration_kg
        }

    def get_organizer(self, obj):
        return {
            'name': {
                'ru': obj.organizer_name_ru,
                'en': obj.organizer_name_en,
                'kg': obj.organizer_name_kg
            },
            'contact': {
                'ru': obj.organizer_contact_ru,
                'en': obj.organizer_contact_en,
                'kg': obj.organizer_contact_kg
            }
        }

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
        return {
            'ru': obj.title_ru,
            'en': obj.title_en,
            'kg': obj.title_kg
        }

    def get_description(self, obj):
        return {
            'ru': obj.description_ru,
            'en': obj.description_en,
            'kg': obj.description_kg
        }

    def get_location(self, obj):
        return {
            'ru': obj.location_ru,
            'en': obj.location_en,
            'kg': obj.location_kg
        }
