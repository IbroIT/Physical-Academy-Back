from rest_framework import viewsets
from ..models_disability_page import DisabilityPage
from ..serializers_disability_page import DisabilityPageSerializer


class DisabilityPageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for disability page content

    GET /api/student-clubs/disabilities-page/
    Optional: ?lang=en (ru by default)
    """

    queryset = DisabilityPage.objects.all().order_by("order", "id")
    serializer_class = DisabilityPageSerializer

    def get_serializer_context(self):
        """Add language to serializer context based on query parameter"""
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "en")  # Default to English

        # Validate language
        if lang not in ["ru", "en", "kg"]:
            lang = "en"

        context["language"] = lang
        return context
