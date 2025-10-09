from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from .models import (
    BoardOfTrustees, AuditCommission, AcademicCouncil,
    TradeUnionBenefit, TradeUnionEvent, TradeUnionStats,
    Commission, AdministrativeDepartment, AdministrativeUnit,
    BoardOfTrusteesStats, AuditCommissionStatistics,
    Leadership, OrganizationStructure, Document
)
from .serializers import (
    BoardOfTrusteesSerializer, AuditCommissionSerializer, AcademicCouncilSerializer,
    TradeUnionBenefitSerializer, TradeUnionEventSerializer, TradeUnionStatsSerializer,
    CommissionSerializer, AdministrativeDepartmentSerializer, AdministrativeUnitSerializer,
    BoardOfTrusteesStatsSerializer, AuditCommissionStatisticsSerializer,
    LeadershipSerializer, OrganizationStructureSerializer, DocumentSerializer
)


@extend_schema_view(
    list=extend_schema(
        summary="Get list of Board of Trustees members",
        description="Retrieve all active Board of Trustees members with multilingual support (ru, kg, en).",
        tags=["Leadership Structure - Board of Trustees"],
        parameters=[
            OpenApiParameter(name='lang', description='Language code (ru, kg, en)', required=False, type=str),
        ]
    ),
    retrieve=extend_schema(
        summary="Get Board of Trustees member details",
        description="Retrieve detailed information about a specific trustee.",
        tags=["Leadership Structure - Board of Trustees"]
    ),
)
class BoardOfTrusteesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Board of Trustees members.
    Provides read-only access with multilingual support.
    """
    serializer_class = BoardOfTrusteesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'name_kg', 'name_en', 'position', 'position_kg', 'position_en']
    ordering_fields = ['order', 'name', 'created_at']
    ordering = ['order', 'name']
    
    def get_queryset(self):
        return BoardOfTrustees.objects.filter(is_active=True)


@extend_schema_view(
    list=extend_schema(
        summary="Get Board of Trustees statistics",
        description="Retrieve statistics for the Board of Trustees page.",
        tags=["Leadership Structure - Board of Trustees"],
        parameters=[
            OpenApiParameter(name='lang', description='Language code (ru, kg, en)', required=False, type=str),
        ]
    ),
)
class BoardOfTrusteesStatsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for Board of Trustees Statistics"""
    serializer_class = BoardOfTrusteesStatsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order']
    ordering = ['order']
    
    def get_queryset(self):
        return BoardOfTrusteesStats.objects.filter(is_active=True)


@extend_schema_view(
    list=extend_schema(
        summary="Get list of Audit Commission members",
        description="Retrieve all active Audit Commission members with multilingual support (ru, kg, en).",
        tags=["Leadership Structure - Audit Commission"],
        parameters=[
            OpenApiParameter(name='lang', description='Language code (ru, kg, en)', required=False, type=str),
        ]
    ),
    retrieve=extend_schema(
        summary="Get Audit Commission member details",
        description="Retrieve detailed information about a specific commission member.",
        tags=["Leadership Structure - Audit Commission"]
    ),
)
class AuditCommissionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Audit Commission members.
    Provides read-only access with multilingual support.
    """
    serializer_class = AuditCommissionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'name_kg', 'name_en', 'position', 'department']
    ordering_fields = ['order', 'name', 'created_at']
    ordering = ['order', 'name']
    
    def get_queryset(self):
        return AuditCommission.objects.filter(is_active=True)


@extend_schema_view(
    list=extend_schema(
        summary="Get Audit Commission statistics",
        description="Retrieve statistics for the Audit Commission page.",
        tags=["Leadership Structure - Audit Commission"],
        parameters=[
            OpenApiParameter(name='lang', description='Language code (ru, kg, en)', required=False, type=str),
        ]
    ),
)
class AuditCommissionStatisticsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for Audit Commission Statistics"""
    serializer_class = AuditCommissionStatisticsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order']
    ordering = ['order']
    
    def get_queryset(self):
        return AuditCommissionStatistics.objects.filter(is_active=True)


@extend_schema_view(
    list=extend_schema(
        summary="Get list of Academic Council members",
        description="Retrieve all active Academic Council members with multilingual support (ru, kg, en).",
        tags=["Leadership Structure - Academic Council"],
        parameters=[
            OpenApiParameter(name='lang', description='Language code (ru, kg, en)', required=False, type=str),
        ]
    ),
    retrieve=extend_schema(
        summary="Get Academic Council member details",
        description="Retrieve detailed information about a specific council member.",
        tags=["Leadership Structure - Academic Council"]
    ),
)
class AcademicCouncilViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Academic Council members.
    Provides read-only access with multilingual support.
    """
    serializer_class = AcademicCouncilSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'name_kg', 'name_en', 'position', 'department']
    ordering_fields = ['order', 'name', 'created_at']
    ordering = ['order', 'name']
    
    def get_queryset(self):
        return AcademicCouncil.objects.filter(is_active=True)


@extend_schema_view(
    list=extend_schema(
        summary="Get list of Trade Union benefits",
        description="Retrieve all active Trade Union benefits with multilingual support (ru, kg, en).",
        tags=["Leadership Structure - Trade Union"],
        parameters=[
            OpenApiParameter(name='lang', description='Language code (ru, kg, en)', required=False, type=str),
        ]
    ),
)
class TradeUnionBenefitViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for Trade Union Benefits"""
    serializer_class = TradeUnionBenefitSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order', 'title']
    ordering = ['order']
    
    def get_queryset(self):
        return TradeUnionBenefit.objects.filter(is_active=True)


@extend_schema_view(
    list=extend_schema(
        summary="Get list of Trade Union events",
        description="Retrieve all active Trade Union events with multilingual support (ru, kg, en).",
        tags=["Leadership Structure - Trade Union"],
        parameters=[
            OpenApiParameter(name='lang', description='Language code (ru, kg, en)', required=False, type=str),
        ]
    ),
)
class TradeUnionEventViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for Trade Union Events"""
    serializer_class = TradeUnionEventSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order', 'title']
    ordering = ['order']
    
    def get_queryset(self):
        return TradeUnionEvent.objects.filter(is_active=True)


@extend_schema_view(
    list=extend_schema(
        summary="Get Trade Union statistics",
        description="Retrieve statistics for the Trade Union page.",
        tags=["Leadership Structure - Trade Union"],
        parameters=[
            OpenApiParameter(name='lang', description='Language code (ru, kg, en)', required=False, type=str),
        ]
    ),
)
class TradeUnionStatsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for Trade Union Statistics"""
    serializer_class = TradeUnionStatsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order']
    ordering = ['order']
    
    def get_queryset(self):
        return TradeUnionStats.objects.filter(is_active=True)


@extend_schema_view(
    list=extend_schema(
        summary="Get list of Commissions",
        description="Retrieve all active commissions with multilingual support (ru, kg, en). Can be filtered by category.",
        tags=["Leadership Structure - Commissions"],
        parameters=[
            OpenApiParameter(name='lang', description='Language code (ru, kg, en)', required=False, type=str),
            OpenApiParameter(name='category', description='Filter by category (academic, quality, student, methodical, all)', required=False, type=str),
        ]
    ),
    retrieve=extend_schema(
        summary="Get Commission details",
        description="Retrieve detailed information about a specific commission.",
        tags=["Leadership Structure - Commissions"]
    ),
)
class CommissionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Commissions.
    Provides read-only access with multilingual support and category filtering.
    """
    serializer_class = CommissionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'name_kg', 'name_en', 'chairman']
    ordering_fields = ['order', 'name', 'created_at']
    ordering = ['order', 'name']
    
    def get_queryset(self):
        return Commission.objects.filter(is_active=True)
    
    @extend_schema(
        summary="Get commissions by category",
        description="Filter commissions by specific category",
        tags=["Leadership Structure - Commissions"]
    )
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get commissions filtered by category"""
        category = request.query_params.get('category', 'all')
        if category and category != 'all':
            queryset = self.get_queryset().filter(category=category)
        else:
            queryset = self.get_queryset()
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(
        summary="Get list of Administrative Departments",
        description="Retrieve all active administrative departments with multilingual support (ru, kg, en).",
        tags=["Leadership Structure - Administrative"],
        parameters=[
            OpenApiParameter(name='lang', description='Language code (ru, kg, en)', required=False, type=str),
        ]
    ),
    retrieve=extend_schema(
        summary="Get Administrative Department details",
        description="Retrieve detailed information about a specific department.",
        tags=["Leadership Structure - Administrative"]
    ),
)
class AdministrativeDepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Administrative Departments.
    Provides read-only access with multilingual support.
    """
    serializer_class = AdministrativeDepartmentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'name_kg', 'name_en', 'head']
    ordering_fields = ['order', 'name', 'created_at']
    ordering = ['order', 'name']
    
    def get_queryset(self):
        return AdministrativeDepartment.objects.filter(is_active=True)


@extend_schema_view(
    list=extend_schema(
        summary="Get list of Administrative Units",
        description="Retrieve all active administrative units with multilingual support (ru, kg, en).",
        tags=["Leadership Structure - Administrative"],
        parameters=[
            OpenApiParameter(name='lang', description='Language code (ru, kg, en)', required=False, type=str),
            OpenApiParameter(name='search', description='Search by name, description, or head', required=False, type=str),
        ]
    ),
    retrieve=extend_schema(
        summary="Get Administrative Unit details",
        description="Retrieve detailed information about a specific unit.",
        tags=["Leadership Structure - Administrative"]
    ),
)
class AdministrativeUnitViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Administrative Units.
    Provides read-only access with multilingual support and search functionality.
    """
    serializer_class = AdministrativeUnitSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'name_kg', 'name_en', 'description', 'head']
    ordering_fields = ['order', 'name', 'created_at']
    ordering = ['order', 'name']
    
    def get_queryset(self):
        return AdministrativeUnit.objects.filter(is_active=True)


# ========== NEW VIEWSETS FOR MISSING APIs ==========

@extend_schema_view(
    list=extend_schema(
        summary="Get list of Leadership members",
        description="Retrieve all active Leadership members (ректорат) with multilingual support.",
        tags=["Leadership Structure - Leadership"],
        parameters=[
            OpenApiParameter(name='lang', description='Language code (ru, kg, en)', required=False, type=str),
            OpenApiParameter(name='leadership_type', description='Filter by leadership type', required=False, type=str),
            OpenApiParameter(name='search', description='Search by name, position, or department', required=False, type=str),
        ]
    ),
    retrieve=extend_schema(
        summary="Get Leadership member details",
        description="Retrieve detailed information about a specific leadership member.",
        tags=["Leadership Structure - Leadership"]
    ),
)
class LeadershipViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Leadership members (ректорат).
    Provides read-only access with multilingual support and filtering.
    """
    serializer_class = LeadershipSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['leadership_type']
    search_fields = ['name', 'name_kg', 'name_en', 'position', 'department']
    ordering_fields = ['order', 'name', 'created_at']
    ordering = ['order', 'name']
    
    def get_queryset(self):
        return Leadership.objects.filter(is_active=True)


@extend_schema_view(
    list=extend_schema(
        summary="Get Organization Structure",
        description="Retrieve hierarchical organization structure with multilingual support.",
        tags=["Leadership Structure - Organization"],
        parameters=[
            OpenApiParameter(name='lang', description='Language code (ru, kg, en)', required=False, type=str),
            OpenApiParameter(name='structure_type', description='Filter by structure type', required=False, type=str),
            OpenApiParameter(name='parent', description='Filter by parent ID (null for root elements)', required=False, type=str),
            OpenApiParameter(name='search', description='Search by name or head', required=False, type=str),
        ]
    ),
    retrieve=extend_schema(
        summary="Get Organization Structure details",
        description="Retrieve detailed information about a specific structure unit.",
        tags=["Leadership Structure - Organization"]
    ),
)
class OrganizationStructureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Organization Structure.
    Provides hierarchical structure with multilingual support.
    """
    serializer_class = OrganizationStructureSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['structure_type', 'parent']
    search_fields = ['name', 'name_kg', 'name_en', 'head']
    ordering_fields = ['order', 'name', 'created_at']
    ordering = ['order', 'name']
    
    def get_queryset(self):
        return OrganizationStructure.objects.filter(is_active=True)
    
    @action(detail=False, methods=['get'])
    def root(self, request):
        """Get root level structure units (without parent)"""
        root_structures = self.get_queryset().filter(parent__isnull=True)
        serializer = self.get_serializer(root_structures, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(
        summary="Get list of Documents",
        description="Retrieve all active documents with multilingual support and filtering.",
        tags=["Leadership Structure - Documents"],
        parameters=[
            OpenApiParameter(name='lang', description='Language code (ru, kg, en)', required=False, type=str),
            OpenApiParameter(name='document_type', description='Filter by document type', required=False, type=str),
            OpenApiParameter(name='is_featured', description='Filter featured documents', required=False, type=bool),
            OpenApiParameter(name='search', description='Search by title or description', required=False, type=str),
        ]
    ),
    retrieve=extend_schema(
        summary="Get Document details",
        description="Retrieve detailed information about a specific document.",
        tags=["Leadership Structure - Documents"]
    ),
)
class DocumentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Documents.
    Provides read-only access with multilingual support and filtering.
    """
    serializer_class = DocumentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['document_type', 'is_featured']
    search_fields = ['title', 'title_kg', 'title_en', 'description', 'document_number']
    ordering_fields = ['order', 'title', 'document_date', 'created_at']
    ordering = ['-document_date', 'order', 'title']
    
    def get_queryset(self):
        return Document.objects.filter(is_active=True)
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured documents"""
        featured_docs = self.get_queryset().filter(is_featured=True)
        serializer = self.get_serializer(featured_docs, many=True)
        return Response(serializer.data)
