from rest_framework import serializers
from .models_instructions import (
    InstructionCategory,
    InstructionDocument,
    ImportantUpdate,
)
from django.conf import settings


class InstructionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionCategory
        fields = ["id", "name_ru", "name_en", "name_kg", "code", "order"]


class InstructionDocumentSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.code")
    downloadUrl = serializers.SerializerMethodField()
    lastUpdated = serializers.SerializerMethodField()

    class Meta:
        model = InstructionDocument
        fields = [
            "id",
            "name_ru",
            "name_en",
            "name_kg",
            "description_ru",
            "description_en",
            "description_kg",
            "category",
            "format",
            "size",
            "version",
            "pages",
            "downloads",
            "tags",
            "downloadUrl",
            "lastUpdated",
        ]

    def get_downloadUrl(self, obj):
        if obj.file:
            return f"{settings.MEDIA_URL}{obj.file}"
        return None

    def get_lastUpdated(self, obj):
        return obj.updated_at.strftime("%b %d, %Y")


class ImportantUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportantUpdate
        fields = [
            "id",
            "title_ru",
            "title_en",
            "title_kg",
            "description_ru",
            "description_en",
            "description_kg",
            "date",
            "order",
        ]


class InstructionsPageDataSerializer(serializers.Serializer):
    title = serializers.SerializerMethodField()
    subtitle = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    documents = serializers.SerializerMethodField()
    importantUpdates = serializers.SerializerMethodField()

    def get_title(self, obj):
        language = self.context.get("language", "en")
        titles = {
            "en": "Instructions and Documents",
            "ru": "Инструкции и документы",
            "kg": "Нускамалар жана документтер",
        }
        return titles.get(language, titles["en"])

    def get_subtitle(self, obj):
        language = self.context.get("language", "en")
        subtitles = {
            "en": "Academic documents and instructions for students and staff",
            "ru": "Академические документы и инструкции для студентов и сотрудников",
            "kg": "Студенттер жана кызматкерлер үчүн академиялык документтер жана нускамалар",
        }
        return subtitles.get(language, subtitles["en"])

    def get_documents(self, obj):
        language = self.context.get("language", "en")
        documents = InstructionDocument.objects.filter(is_active=True).select_related(
            "category"
        )

        serializer = InstructionDocumentSerializer(documents, many=True)
        documents_data = serializer.data

        # Localize the fields based on language
        for doc in documents_data:
            doc["name"] = doc[f"name_{language}"]
            doc["description"] = doc[f"description_{language}"]
            doc.pop("name_ru")
            doc.pop("name_en")
            doc.pop("name_kg")
            doc.pop("description_ru")
            doc.pop("description_en")
            doc.pop("description_kg")

        return documents_data

    def get_importantUpdates(self, obj):
        language = self.context.get("language", "en")
        updates = ImportantUpdate.objects.filter(is_active=True).order_by(
            "order", "-actual_date"
        )

        serializer = ImportantUpdateSerializer(updates, many=True)
        updates_data = serializer.data

        # Localize the fields based on language
        for update in updates_data:
            update["title"] = update[f"title_{language}"]
            update["description"] = update[f"description_{language}"]
            update.pop("title_ru")
            update.pop("title_en")
            update.pop("title_kg")
            update.pop("description_ru")
            update.pop("description_en")
            update.pop("description_kg")

        return updates_data
