# COMMENTED OUT: Ebilim backend not needed - using i18n translations on frontend instead

"""
from rest_framework import serializers
from .models_ebilim import EbilimStat, EbilimQuickLink, EbilimSystemStatus
from django.utils.translation import get_language


class EbilimStatSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()

    class Meta:
        model = EbilimStat
        fields = ["key", "value", "label"]

    def get_label(self, obj):
        lang = get_language()
        if lang == "ru":
            return obj.label_ru
        elif lang == "kg":
            return obj.label_kg
        return obj.label_en


class EbilimQuickLinkSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = EbilimQuickLink
        fields = ["name", "url", "icon"]

    def get_name(self, obj):
        lang = get_language()
        if lang == "ru":
            return obj.name_ru
        elif lang == "kg":
            return obj.name_kg
        return obj.name_en


class EbilimSystemStatusSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source="get_status_display")
    message = serializers.SerializerMethodField()

    class Meta:
        model = EbilimSystemStatus
        fields = [
            "status",
            "status_display",
            "message",
            "last_update",
            "support_email",
            "support_phone",
        ]

    def get_message(self, obj):
        lang = get_language()
        if lang == "ru":
            return obj.message_ru
        elif lang == "kg":
            return obj.message_kg
        return obj.message_en


class EbilimPageDataSerializer(serializers.Serializer):
    stats = EbilimStatSerializer(many=True)
    quick_links = EbilimQuickLinkSerializer(many=True)
    system_status = EbilimSystemStatusSerializer()
"""
