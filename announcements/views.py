from rest_framework import generics
from rest_framework.response import Response
from .models import Announcement
from .serializers import AnnouncementSerializer


class AnnouncementListAPIView(generics.ListAPIView):
    """
    API для получения списка всех активных объявлений.
    Поддерживает фильтрацию по языку через параметр ?lang=ru/en/kg
    Возвращает объявления с переводами и галереей изображений.
    """

    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        return (
            Announcement.objects.filter(is_active=True)
            .prefetch_related("translations", "gallery_images")
            .order_by("order", "-created_at")
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset, many=True, context={"request": request}
        )
        return Response(
            {
                "success": True,
                "announcements": serializer.data,
                "count": len(serializer.data),
            }
        )


class AnnouncementDetailAPIView(generics.RetrieveAPIView):
    """
    API для получения детальной информации об объявлении.
    Поддерживает фильтрацию по языку через параметр ?lang=ru/en/kg
    Возвращает объявление с полным содержимым, переводами и галереей изображений.
    """

    queryset = Announcement.objects.filter(is_active=True)
    serializer_class = AnnouncementSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Announcement.objects.filter(is_active=True).prefetch_related(
            "translations", "gallery_images"
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={"request": request})
        return Response({"success": True, "announcement": serializer.data})
