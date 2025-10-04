from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Leadership, Accreditation, OrganizationStructure, DownloadableDocument
from .serializers import (
    LeadershipSerializer, AccreditationSerializer, 
    OrganizationStructureSerializer, DownloadableDocumentSerializer
)


@extend_schema_view(
    list=extend_schema(
        summary="Get list of leadership members",
        description="Retrieve a list of all active leadership members with multilingual support.",
        tags=["Leadership"]
    ),
    retrieve=extend_schema(
        summary="Get leadership member details", 
        description="Retrieve detailed information about a specific leadership member.",
        tags=["Leadership"]
    ),
)
class LeadershipViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Leadership model.
    Provides read-only access to leadership information with multilingual support.
    """
    serializer_class = LeadershipSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['leadership_type', 'department', 'is_director', 'is_active']
    search_fields = ['name', 'name_kg', 'name_en', 'position', 'department']
    ordering_fields = ['order', 'name', 'created_at']
    ordering = ['order', 'name']
    
    def get_queryset(self):
        """Filter active leadership members"""
        return Leadership.objects.filter(is_active=True)
    
    @extend_schema(
        summary="Get directors only",
        description="Retrieve all directors (is_director=True)",
        tags=["Leadership"]
    )
    @action(detail=False, methods=['get'])
    def directors(self, request):
        """Get all directors"""
        queryset = self.get_queryset().filter(is_director=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        summary="Get department heads",
        description="Retrieve all department heads and faculty deans",
        tags=["Leadership"]
    )
    @action(detail=False, methods=['get'])
    def department_heads(self, request):
        """Get department heads and deans"""
        queryset = self.get_queryset().filter(
            leadership_type__in=['department_head', 'dean']
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(
        summary="Get list of accreditations",
        description="Retrieve a list of all active accreditations and certifications.",
        tags=["Accreditations"]
    ),
    retrieve=extend_schema(
        summary="Get accreditation details",
        description="Retrieve detailed information about a specific accreditation.",
        tags=["Accreditations"]
    ),
)
class AccreditationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Accreditation model.
    Provides read-only access to accreditation information.
    """
    serializer_class = AccreditationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['accreditation_type', 'is_active']
    search_fields = ['name', 'name_kg', 'name_en', 'organization']
    ordering_fields = ['order', 'issue_date', 'name']
    ordering = ['order', '-issue_date']
    
    def get_queryset(self):
        """Filter active accreditations"""
        return Accreditation.objects.filter(is_active=True)
    
    @extend_schema(
        summary="Get active/valid accreditations",
        description="Retrieve only currently valid accreditations (not expired)",
        tags=["Accreditations"]
    )
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get only currently valid accreditations"""
        queryset = self.get_queryset()
        valid_accreditations = [acc for acc in queryset if acc.is_valid]
        serializer = self.get_serializer(valid_accreditations, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(
        summary="Get organizational structure",
        description="Retrieve the complete organizational structure with multilingual support.",
        tags=["Organization Structure"]
    ),
    retrieve=extend_schema(
        summary="Get department details",
        description="Retrieve detailed information about a specific department or unit.",
        tags=["Organization Structure"]
    ),
)
class OrganizationStructureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for OrganizationStructure model.
    Provides read-only access to organizational structure with multilingual support.
    """
    serializer_class = OrganizationStructureSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['structure_type', 'parent', 'is_active']
    search_fields = ['name_ru', 'name_en', 'name_ky', 'head_name_ru']
    ordering_fields = ['order', 'name_ru']
    ordering = ['structure_type', 'order', 'name_ru']
    
    def get_queryset(self):
        """Filter active departments"""
        return OrganizationStructure.objects.filter(is_active=True)
    
    @extend_schema(
        summary="Get hierarchical structure",
        description="Retrieve the organizational structure in hierarchical format (top-level departments with their children)",
        tags=["Organization Structure"]
    )
    @action(detail=False, methods=['get'])
    def hierarchy(self, request):
        """Get organizational structure in hierarchical format"""
        # Get top-level departments (no parent)
        top_level = self.get_queryset().filter(parent__isnull=True)
        serializer = self.get_serializer(top_level, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(
        summary="Get downloadable documents",
        description="Retrieve a list of all available documents for download.",
        tags=["Documents"]
    ),
    retrieve=extend_schema(
        summary="Get document details",
        description="Retrieve detailed information about a specific document.",
        tags=["Documents"]
    ),
)
class DownloadableDocumentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for DownloadableDocument model.
    Provides read-only access to downloadable documents with multilingual support.
    """
    serializer_class = DownloadableDocumentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['title_ru', 'title_en', 'title_ky', 'description_ru']
    ordering_fields = ['created_at', 'title_ru']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """Filter active documents"""
        return DownloadableDocument.objects.filter(is_active=True)
