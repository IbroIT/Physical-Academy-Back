from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from .models import BannerSlide

class BannerSlideSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = BannerSlide
        fields = ['id', 'title', 'image_url', 'alt_text', 'order']

    @extend_schema_field(OpenApiTypes.STR)
    def get_image_url(self, obj):
        if not obj.image:
            return None
        try:
            return obj.image.url
        except Exception:
            return str(obj.image)