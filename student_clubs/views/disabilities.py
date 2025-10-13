from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models_disabilities import (
    DisabilitySupportService,
    DisabilityContactPerson,
    DisabilityResource,
    DisabilityEmergencyContact,
)
from ..serializers_disabilities import (
    DisabilitySupportServiceSerializer,
    DisabilityContactPersonSerializer,
    DisabilityResourceSerializer,
    DisabilityEmergencyContactSerializer,
    DisabilitiesPageDataSerializer,
)


class DisabilitySupportServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoints for disability support services"""

    queryset = DisabilitySupportService.objects.all().order_by("order")
    serializer_class = DisabilitySupportServiceSerializer

    def get_serializer_context(self):
        """Add language to serializer context based on query parameter"""
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "ru")
        # Validate language
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"
        context["language"] = lang
        return context


class DisabilityContactPersonViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoints for disability contact persons"""

    queryset = DisabilityContactPerson.objects.all().order_by("order")
    serializer_class = DisabilityContactPersonSerializer

    def get_serializer_context(self):
        """Add language to serializer context based on query parameter"""
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "ru")
        # Validate language
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"
        context["language"] = lang
        return context


class DisabilityResourceViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoints for disability resources"""

    queryset = DisabilityResource.objects.all().order_by("order")
    serializer_class = DisabilityResourceSerializer

    def get_serializer_context(self):
        """Add language to serializer context based on query parameter"""
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "ru")
        # Validate language
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"
        context["language"] = lang
        return context


class DisabilityEmergencyContactViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoints for disability emergency contacts"""

    queryset = DisabilityEmergencyContact.objects.all().order_by("order")
    serializer_class = DisabilityEmergencyContactSerializer

    def get_serializer_context(self):
        """Add language to serializer context based on query parameter"""
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "ru")
        # Validate language
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"
        context["language"] = lang
        return context


class DisabilitiesPageDataViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that returns all data needed for the disabilities support page
    GET /api/student-clubs/disabilities-page/
    Optional: ?lang=en (ru by default)
    """

    serializer_class = DisabilitiesPageDataSerializer

    def get_serializer_context(self):
        """Add language to serializer context based on query parameter"""
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "ru")
        # Validate language
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"
        context["language"] = lang
        return context

    def list(self, request, *args, **kwargs):
        """Return all data for the disabilities support page"""
        # Get all the data we need
        services = DisabilitySupportService.objects.all().order_by("order")
        contacts = DisabilityContactPerson.objects.all().order_by("order")
        resources = DisabilityResource.objects.all().order_by("order")

        # Get emergency contact (single object or empty list)
        try:
            emergency_obj = (
                DisabilityEmergencyContact.objects.all().order_by("order").first()
            )
            emergency = emergency_obj if emergency_obj else None
        except DisabilityEmergencyContact.DoesNotExist:
            emergency = None

        # Create a single object with all the data
        page_data = {
            "support_services": services,
            "contacts": contacts,
            "resources": resources,
            "emergency": emergency,
        }

        # Serialize it
        serializer = self.get_serializer(page_data)
        return Response(serializer.data)
