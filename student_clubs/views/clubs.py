from rest_framework import viewsets, filters, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from ..models import (
    Club,
    ClubCategory,
    ClubLeader,
    ClubStats,
    StudentProfile,
    ClubMembership,
)
from ..serializers import (
    ClubListSerializer,
    ClubDetailSerializer,
    ClubCategorySerializer,
    ClubLeaderSerializer,
    ClubStatsSerializer,
    # ClubPageSerializer,
    StudentProfileSerializer,
    StudentProfileListSerializer,
    StudentProfileCreateSerializer,
    ClubMembershipSerializer,
    ClubMembershipCreateSerializer,
    StudentClubsSerializer,
)


class BaseLanguageViewSet(viewsets.ModelViewSet):
    """Базовый ViewSet с поддержкой языка"""

    def get_serializer_context(self):
        context = super().get_serializer_context()
        # Only use explicit ?lang= query parameter. Default to Russian.
        language = self.request.query_params.get("lang", "ru")

        # Normalize legacy code 'ky' to 'kg' for backward compatibility
        if language == "ky":
            language = "kg"

        # Support only ru, en, kg
        if language not in ["ru", "en", "kg"]:
            language = "ru"

        context["language"] = language
        return context


class ClubCategoryViewSet(BaseLanguageViewSet):
    """API для категорий клубов"""

    queryset = ClubCategory.objects.all()
    serializer_class = ClubCategorySerializer
    lookup_field = "slug"

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return ClubCategory.objects.none()
        return ClubCategory.objects.all().order_by("order", "name_ru")


class ClubViewSet(BaseLanguageViewSet):
    """API для клубов с фильтрацией и поиском"""

    queryset = Club.objects.filter(is_active=True)
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["category", "status", "category__slug"]
    search_fields = [
        "name_ru",
        "name_en",
        "name_kg",
        "description_ru",
        "description_en",
        "description_kg",
        "tags",
    ]
    ordering_fields = ["members_count", "created_at", "order"]
    ordering = ["order", "-members_count"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ClubDetailSerializer
        return ClubListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return queryset.none()

        # Фильтрация по параметру featured
        featured = self.request.query_params.get("featured", None)
        if featured and featured.lower() in ["true", "1", "yes"]:
            queryset = queryset.filter(is_featured=True)

        # Фильтрация по категории через slug
        category_slug = self.request.query_params.get("category_slug", None)
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        return queryset

    @action(detail=True, methods=["post"])
    def join(self, request, pk=None):
        """Endpoint для вступления в клуб"""
        club = self.get_object()
        student_id = request.data.get("student_id")

        if not student_id:
            return Response(
                {"error": "Student ID is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            student = StudentProfile.objects.get(pk=student_id)
        except StudentProfile.DoesNotExist:
            return Response(
                {"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Проверяем, не состоит ли уже студент в этом клубе
        if ClubMembership.objects.filter(club=club, student=student).exists():
            return Response(
                {"error": "Student is already a member of this club"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Создаем новое членство
        membership = ClubMembership.objects.create(
            club=club, student=student, status="pending"
        )

        # Обновляем счетчик членов в клубе
        club.members_count = ClubMembership.objects.filter(club=club).count()
        club.save()

        return Response(
            ClubMembershipSerializer(membership).data, status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=["post"])
    def leave(self, request, pk=None):
        """Endpoint для выхода из клуба"""
        club = self.get_object()
        student_id = request.data.get("student_id")

        if not student_id:
            return Response(
                {"error": "Student ID is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            student = StudentProfile.objects.get(pk=student_id)
        except StudentProfile.DoesNotExist:
            return Response(
                {"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Проверяем, состоит ли студент в этом клубе
        try:
            membership = ClubMembership.objects.get(club=club, student=student)
        except ClubMembership.DoesNotExist:
            return Response(
                {"error": "Student is not a member of this club"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Удаляем членство
        membership.delete()

        # Обновляем счетчик членов в клубе
        club.members_count = ClubMembership.objects.filter(club=club).count()
        club.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ClubLeaderViewSet(BaseLanguageViewSet):
    """API для лидеров клубов"""

    queryset = ClubLeader.objects.all()
    serializer_class = ClubLeaderSerializer

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return ClubLeader.objects.none()
        return ClubLeader.objects.all().order_by("order", "name_ru")


class ClubStatsViewSet(BaseLanguageViewSet):
    """API для статистики клубов"""

    queryset = ClubStats.objects.all()
    serializer_class = ClubStatsSerializer

    def get_queryset(self):
        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return ClubStats.objects.none()
        return ClubStats.objects.all().order_by("order")


class StudentProfileViewSet(BaseLanguageViewSet):
    """API для профилей студентов"""

    queryset = StudentProfile.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "first_name_ru",
        "last_name_ru",
        "first_name_en",
        "last_name_en",
        "first_name_kg",
        "last_name_kg",
        "email",
        "phone",
        "student_id",
    ]

    def get_serializer_class(self):
        if self.action == "create":
            return StudentProfileCreateSerializer
        if self.action == "list":
            return StudentProfileListSerializer
        return StudentProfileSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return queryset.none()

        # Фильтрация по email или student_id для поиска конкретного студента
        email = self.request.query_params.get("email", None)
        student_id = self.request.query_params.get("student_id", None)

        if email:
            queryset = queryset.filter(email=email)
        if student_id:
            queryset = queryset.filter(student_id=student_id)

        return queryset

    @action(detail=True)
    def clubs(self, request, pk=None):
        """Получить все клубы, в которых состоит студент"""
        student = self.get_object()
        memberships = ClubMembership.objects.filter(student=student).select_related(
            "club"
        )
        clubs_data = []

        for membership in memberships:
            club_data = ClubListSerializer(
                membership.club, context=self.get_serializer_context()
            ).data
            club_data["membership"] = {
                "id": membership.id,
                "status": membership.status,
                "joined_at": membership.joined_at,
                "role": membership.role,
            }
            clubs_data.append(club_data)

        return Response(clubs_data)


class ClubMembershipViewSet(BaseLanguageViewSet):
    """API для управления членством в клубах"""

    queryset = ClubMembership.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["club", "student", "status"]

    def get_serializer_class(self):
        if self.action == "create":
            return ClubMembershipCreateSerializer
        return ClubMembershipSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Check for swagger schema generation
        if getattr(self, "swagger_fake_view", False):
            return queryset.none()

        # Фильтрация по клубу через slug
        club_slug = self.request.query_params.get("club_slug", None)
        if club_slug:
            queryset = queryset.filter(club__slug=club_slug)

        return queryset

    def perform_create(self, serializer):
        """При создании обновляем счетчик членов клуба"""
        membership = serializer.save()
        club = membership.club
        club.members_count = ClubMembership.objects.filter(club=club).count()
        club.save()

    def perform_destroy(self, instance):
        """При удалении обновляем счетчик членов клуба"""
        club = instance.club
        super().perform_destroy(instance)
        club.members_count = ClubMembership.objects.filter(club=club).count()
        club.save()

    @action(detail=False, methods=["get"])
    def student_clubs(self, request):
        """Получить все клубы и статус участия текущего студента в них"""
        student_id = request.query_params.get("student_id")
        if not student_id:
            return Response(
                {"error": "student_id parameter is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            student = StudentProfile.objects.get(pk=student_id)
        except StudentProfile.DoesNotExist:
            return Response(
                {"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Получаем все клубы и информацию о членстве студента
        clubs = Club.objects.filter(is_active=True).order_by("order", "name_ru")
        memberships = ClubMembership.objects.filter(student=student)

        # Словарь для быстрого доступа к информации о членстве по ID клуба
        membership_dict = {membership.club_id: membership for membership in memberships}

        serializer = StudentClubsSerializer(
            clubs,
            many=True,
            context={"memberships": membership_dict, **self.get_serializer_context()},
        )
        return Response(serializer.data)
