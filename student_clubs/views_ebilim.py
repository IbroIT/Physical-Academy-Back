# COMMENTED OUT: Ebilim backend not needed - using i18n translations on frontend instead

"""
from rest_framework import viewsets, views
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models_ebilim import EbilimStat, EbilimQuickLink, EbilimSystemStatus
from .serializers_ebilim import (
    EbilimStatSerializer,
    EbilimQuickLinkSerializer,
    EbilimSystemStatusSerializer,
    EbilimPageDataSerializer,
)


class EbilimStatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EbilimStat.objects.all().order_by("order")
    serializer_class = EbilimStatSerializer


class EbilimQuickLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EbilimQuickLink.objects.filter(is_active=True).order_by("order")
    serializer_class = EbilimQuickLinkSerializer


class EbilimSystemStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EbilimSystemStatus.objects.all()
    serializer_class = EbilimSystemStatusSerializer

    def get_queryset(self):
        # Return only the most recent status
        return EbilimSystemStatus.objects.all().order_by("-last_update")[:1]


@method_decorator(cache_page(60 * 5), name="dispatch")  # Cache for 5 minutes
class EbilimPageDataView(views.APIView):
    def get(self, request):
        stats = EbilimStat.objects.all().order_by("order")
        quick_links = EbilimQuickLink.objects.filter(is_active=True).order_by("order")
        system_status = EbilimSystemStatus.objects.order_by("-last_update").first()

        data = {
            "stats": stats,
            "quick_links": quick_links,
            "system_status": system_status,
        }

        serializer = EbilimPageDataSerializer(data)
        return Response(serializer.data)


class EbilimPageDataViewSet(viewsets.ViewSet):
    # ViewSet wrapper so ebilim appears in router URLs.
    # Delegates to existing EbilimPageDataView.

    def list(self, request, *args, **kwargs):
        view = EbilimPageDataView.as_view()
        return view(request, *args, **kwargs)
"""
