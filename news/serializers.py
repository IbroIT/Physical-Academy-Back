from rest_framework import serializers
from .models import News, NewsTranslation, NewsImage


class NewsTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTranslation
        fields = ["language", "title", "description", "category", "content"]


class NewsImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = NewsImage
        fields = ["id", "image_url", "order"]

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class NewsSerializer(serializers.ModelSerializer):
    translations = NewsTranslationSerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()
    gallery_images = NewsImageSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = [
            "id",
            "image_url",
            "gallery_images",
            "is_active",
            "order",
            "created_at",
            "translations",
        ]

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        language = request.query_params.get("lang", "ru") if request else "ru"

        # Находим перевод для запрошенного языка
        translation = instance.translations.filter(language=language).first()

        if translation:
            data["title"] = translation.title
            data["description"] = translation.description
            data["category"] = translation.category
            data["content"] = translation.content
        else:
            # Fallback на русский язык
            ru_translation = instance.translations.filter(language="ru").first()
            if ru_translation:
                data["title"] = ru_translation.title
                data["description"] = ru_translation.description
                data["category"] = ru_translation.category
                data["content"] = ru_translation.content
            else:
                # Если нет даже русского перевода, берем первый доступный
                first_translation = instance.translations.first()
                if first_translation:
                    data["title"] = first_translation.title
                    data["description"] = first_translation.description
                    data["category"] = first_translation.category
                    data["content"] = first_translation.content

        return data
