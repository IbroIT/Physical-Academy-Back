from rest_framework import serializers
from .models import (
    IPChainInfo,
    IPChainInfoTranslation,
    IPChainStatistic,
    IPChainStatisticTranslation,
    Patent,
    PatentTranslation,
    BlockchainFeature,
    BlockchainFeatureTranslation,
    IPChainBenefit,
    IPChainBenefitTranslation,
    BlockchainData,
    BlockchainDataTranslation,
)


class IPChainInfoSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    subtitle = serializers.SerializerMethodField()

    class Meta:
        model = IPChainInfo
        fields = ["id", "title", "subtitle", "order"]

    def get_title(self, obj):
        language = self.context.get("language", "ru")
        translation = obj.translations.filter(language=language).first()
        return translation.title if translation else obj.title

    def get_subtitle(self, obj):
        language = self.context.get("language", "ru")
        translation = obj.translations.filter(language=language).first()
        return translation.subtitle if translation else obj.subtitle


class IPChainStatisticSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()

    class Meta:
        model = IPChainStatistic
        fields = ["id", "value", "label", "order"]

    def get_label(self, obj):
        language = self.context.get("language", "ru")
        translation = obj.translations.filter(language=language).first()
        return translation.label if translation else ""


class PatentSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    full_description = serializers.SerializerMethodField()
    technologies = serializers.SerializerMethodField()
    applications = serializers.SerializerMethodField()

    class Meta:
        model = Patent
        fields = [
            "id",
            "title",
            "number",
            "description",
            "status",
            "year",
            "date",
            "icon",
            "full_description",
            "technologies",
            "applications",
            "order",
        ]

    def get_translation(self, obj):
        language = self.context.get("language", "ru")
        return obj.translations.filter(language=language).first()

    def get_title(self, obj):
        translation = self.get_translation(obj)
        return translation.title if translation else ""

    def get_description(self, obj):
        translation = self.get_translation(obj)
        return translation.description if translation else ""

    def get_full_description(self, obj):
        translation = self.get_translation(obj)
        return translation.full_description if translation else ""

    def get_technologies(self, obj):
        translation = self.get_translation(obj)
        return translation.technologies if translation else []

    def get_applications(self, obj):
        translation = self.get_translation(obj)
        return translation.applications if translation else []


class BlockchainFeatureSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = BlockchainFeature
        fields = ["id", "title", "description", "icon", "order"]

    def get_title(self, obj):
        language = self.context.get("language", "ru")
        translation = obj.translations.filter(language=language).first()
        return translation.title if translation else ""

    def get_description(self, obj):
        language = self.context.get("language", "ru")
        translation = obj.translations.filter(language=language).first()
        return translation.description if translation else ""


class IPChainBenefitSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = IPChainBenefit
        fields = ["id", "title", "description", "icon", "order"]

    def get_title(self, obj):
        language = self.context.get("language", "ru")
        translation = obj.translations.filter(language=language).first()
        return translation.title if translation else ""

    def get_description(self, obj):
        language = self.context.get("language", "ru")
        translation = obj.translations.filter(language=language).first()
        return translation.description if translation else ""


class BlockchainDataSerializer(serializers.ModelSerializer):
    current_block_label = serializers.SerializerMethodField()
    ip_registrations_label = serializers.SerializerMethodField()
    smart_contracts_label = serializers.SerializerMethodField()
    network_hash_label = serializers.SerializerMethodField()

    class Meta:
        model = BlockchainData
        fields = [
            "id",
            "current_block",
            "current_block_label",
            "ip_registrations",
            "ip_registrations_label",
            "smart_contracts",
            "smart_contracts_label",
            "network_hash",
            "network_hash_label",
            "order",
            "updated_at",
        ]

    def get_translation(self, obj):
        language = self.context.get("language", "ru")
        return obj.translations.filter(language=language).first()

    def get_current_block_label(self, obj):
        translation = self.get_translation(obj)
        return translation.current_block_label if translation else "Текущий блок"

    def get_ip_registrations_label(self, obj):
        translation = self.get_translation(obj)
        return translation.ip_registrations_label if translation else "Регистраций IP"

    def get_smart_contracts_label(self, obj):
        translation = self.get_translation(obj)
        return translation.smart_contracts_label if translation else "Смарт-контрактов"

    def get_network_hash_label(self, obj):
        translation = self.get_translation(obj)
        return translation.network_hash_label if translation else "Хэш сети"
