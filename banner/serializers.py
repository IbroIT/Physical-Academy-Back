from rest_framework import serializers
from .models import BannerSlide

class BannerSlideSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = BannerSlide
        fields = ['id', 'title', 'image_url', 'alt_text', 'order']

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None