from rest_framework import generics
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer


class NewsListAPIView(generics.ListAPIView):
    """
    API для получения списка всех активных новостей.
    Поддерживает фильтрацию по языку через параметр ?lang=ru/en/kg
    Возвращает новости с переводами и галереей изображений.
    """

    serializer_class = NewsSerializer

    def get_queryset(self):
        return (
            News.objects.filter(is_active=True)
            .prefetch_related("translations", "gallery_images")
            .order_by("order", "-created_at")
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset, many=True, context={"request": request}
        )
        return Response(
            {"success": True, "news": serializer.data, "count": len(serializer.data)}
        )


class NewsDetailAPIView(generics.RetrieveAPIView):
    """
    API для получения детальной информации о новости.
    Поддерживает фильтрацию по языку через параметр ?lang=ru/en/kg
    Возвращает новость с полным содержимым, переводами и галереей изображений.
    """

    queryset = News.objects.filter(is_active=True)
    serializer_class = NewsSerializer
    lookup_field = "id"

    def get_queryset(self):
        return News.objects.filter(is_active=True).prefetch_related(
            "translations", "gallery_images"
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={"request": request})
        return Response({"success": True, "news": serializer.data})
