from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from ..models.contact_social import (
    StudentContactInfo,
    SocialNetworkAccount,
    SocialCommunity,
)
from ..serializers.contact_social import (
    StudentContactInfoSerializer,
    SocialNetworkAccountSerializer,
    SocialCommunitySerializer,
)


class StudentContactInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """API for student contact information"""

    queryset = StudentContactInfo.objects.filter(is_active=True).order_by("order")
    serializer_class = StudentContactInfoSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    @action(detail=False, methods=["get"])
    def featured(self, request):
        """Get featured contact information only"""
        queryset = self.get_queryset().filter(is_featured=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SocialNetworkAccountViewSet(viewsets.ReadOnlyModelViewSet):
    """API for social network accounts"""

    queryset = SocialNetworkAccount.objects.filter(is_active=True).order_by("order")
    serializer_class = SocialNetworkAccountSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    @action(detail=False, methods=["get"])
    def featured(self, request):
        """Get featured social accounts only"""
        queryset = self.get_queryset().filter(is_featured=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    @action(detail=False, methods=["get"])
    def official(self, request):
        """Get official social accounts only"""
        queryset = self.get_queryset().filter(is_official=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SocialCommunityViewSet(viewsets.ReadOnlyModelViewSet):
    """API for student social communities"""

    queryset = SocialCommunity.objects.filter(is_active=True).order_by("order")
    serializer_class = SocialCommunitySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    @action(detail=False, methods=["get"])
    def featured(self, request):
        """Get featured communities only"""
        queryset = self.get_queryset().filter(is_featured=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    @action(detail=False, methods=["get"])
    def verified(self, request):
        """Get verified communities only"""
        queryset = self.get_queryset().filter(is_verified=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ContactSocialPageDataViewSet(viewsets.ViewSet):
    """API for getting all contact and social data in a single request"""

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    @action(detail=False, methods=["get"])
    def contact_info_page(self, request):
        """Get all data for the contact info page in a single request"""
        language = request.query_params.get("lang", "ru")
        context = {"language": language, "request": request}

        contact_info = StudentContactInfo.objects.filter(is_active=True).order_by(
            "order"
        )
        featured_contacts = contact_info.filter(is_featured=True)

        data = {
            "contact_info": StudentContactInfoSerializer(
                contact_info, many=True, context=context
            ).data,
            "featured_contacts": StudentContactInfoSerializer(
                featured_contacts, many=True, context=context
            ).data,
        }

        return Response(data)

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    @action(detail=False, methods=["get"])
    def social_page(self, request):
        """Get all data for the social page in a single request"""
        language = request.query_params.get("lang", "ru")
        context = {"language": language, "request": request}

        social_accounts = SocialNetworkAccount.objects.filter(is_active=True).order_by(
            "order"
        )
        featured_accounts = social_accounts.filter(is_featured=True)
        official_accounts = social_accounts.filter(is_official=True)

        communities = SocialCommunity.objects.filter(is_active=True).order_by("order")
        featured_communities = communities.filter(is_featured=True)
        verified_communities = communities.filter(is_verified=True)

        data = {
            "social_accounts": SocialNetworkAccountSerializer(
                social_accounts, many=True, context=context
            ).data,
            "featured_accounts": SocialNetworkAccountSerializer(
                featured_accounts, many=True, context=context
            ).data,
            "official_accounts": SocialNetworkAccountSerializer(
                official_accounts, many=True, context=context
            ).data,
            "communities": SocialCommunitySerializer(
                communities, many=True, context=context
            ).data,
            "featured_communities": SocialCommunitySerializer(
                featured_communities, many=True, context=context
            ).data,
            "verified_communities": SocialCommunitySerializer(
                verified_communities, many=True, context=context
            ).data,
        }

        return Response(data)
