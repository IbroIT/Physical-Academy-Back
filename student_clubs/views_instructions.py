from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models_instructions import (
    InstructionCategory,
    InstructionDocument,
    ImportantUpdate,
)
from .serializers_instructions import (
    InstructionCategorySerializer,
    InstructionDocumentSerializer,
    ImportantUpdateSerializer,
    InstructionsPageDataSerializer,
)


class InstructionCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for instruction categories.
    """

    queryset = InstructionCategory.objects.all().order_by("order")
    serializer_class = InstructionCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class InstructionDocumentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for instruction documents.
    """

    queryset = InstructionDocument.objects.filter(is_active=True).order_by(
        "order", "-updated_at"
    )
    serializer_class = InstructionDocumentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ["category__code"]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.downloads += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ImportantUpdateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for important updates.
    """

    queryset = ImportantUpdate.objects.filter(is_active=True).order_by(
        "order", "-actual_date"
    )
    serializer_class = ImportantUpdateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class InstructionsPageDataViewSet(viewsets.ViewSet):
    """
    API endpoint for the complete instructions page data.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request):
        language = request.query_params.get("lang", "en")
        if language not in ["en", "ru", "kg"]:
            language = "en"

        serializer = InstructionsPageDataSerializer(
            {"request": request}, context={"language": language, "request": request}
        )
        return Response(serializer.data)
