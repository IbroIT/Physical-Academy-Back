from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models_disabilities import (
    DisabilitySupportService,
    DisabilityContactPerson,
    DisabilityResource,
    DisabilityEmergencyContact,
)
from .serializers_disabilities import (
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

    queryset = DisabilityEmergencyContact.objects.all().order_by("id")
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


class DisabilitiesPageDataViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """API endpoint to get all disabilities page data in a single request"""

    def list(self, request):
        lang = request.query_params.get("lang", "ru")
        # Validate language
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"

        # Get all needed data
        support_services = DisabilitySupportService.objects.all().order_by("order")
        contacts = DisabilityContactPerson.objects.all().order_by("order")
        resources = DisabilityResource.objects.all().order_by("order")

        # Get emergency contact (single object)
        try:
            emergency = DisabilityEmergencyContact.objects.all().order_by("id").first()
        except DisabilityEmergencyContact.DoesNotExist:
            emergency = None

        # Prepare context with language
        context = {"language": lang}

        # Serialize each component
        support_services_serializer = DisabilitySupportServiceSerializer(
            support_services, many=True, context=context
        )
        contacts_serializer = DisabilityContactPersonSerializer(
            contacts, many=True, context=context
        )
        resources_serializer = DisabilityResourceSerializer(
            resources, many=True, context=context
        )
        emergency_serializer = (
            DisabilityEmergencyContactSerializer(emergency, context=context)
            if emergency
            else None
        )

        # Combine data
        data = {
            "support_services": support_services_serializer.data,
            "contacts": contacts_serializer.data,
            "resources": resources_serializer.data,
            "emergency": emergency_serializer.data if emergency else None,
        }

        return Response(data)
