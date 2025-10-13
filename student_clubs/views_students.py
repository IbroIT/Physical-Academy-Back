from rest_framework import viewsets, filters, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models_students import StudentProfile, ClubMembership
from .serializers_students import (
    StudentProfileSerializer,
    StudentProfileListSerializer,
    StudentProfileCreateSerializer,
    ClubMembershipSerializer,
    ClubMembershipCreateSerializer,
    StudentClubsSerializer,
)
from .views import BaseLanguageViewSet
from .models import Club


class StudentProfileViewSet(BaseLanguageViewSet):
    """API для профилей студентов"""

    queryset = StudentProfile.objects.filter(is_active=True)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["year_of_study"]
    search_fields = [
        "full_name_ru",
        "full_name_en",
        "full_name_kg",
        "email",
        "faculty_ru",
        "major_ru",
    ]

    def get_serializer_class(self):
        if self.action == "create":
            return StudentProfileCreateSerializer
        elif self.action == "list":
            return StudentProfileListSerializer
        elif self.action == "my_clubs":
            return StudentClubsSerializer
        return StudentProfileSerializer

    def get_queryset(self):
        queryset = StudentProfile.objects.filter(is_active=True)

        # Фильтрация по факультету (поиск по всем языковым версиям)
        faculty = self.request.query_params.get("faculty")
        if faculty:
            queryset = queryset.filter(
                Q(faculty_ru__icontains=faculty)
                | Q(faculty_en__icontains=faculty)
                | Q(faculty_kg__icontains=faculty)
            )

        # Фильтрация по интересам
        interests = self.request.query_params.get("interests")
        if interests:
            interests_list = interests.split(",")
            for interest in interests_list:
                queryset = queryset.filter(interests__contains=[interest.strip()])

        # Проверка на Swagger
        if getattr(self, "swagger_fake_view", False):
            return StudentProfile.objects.none()

        return queryset

    @action(detail=True, methods=["get"])
    def my_clubs(self, request, pk=None):
        """
        Получить список клубов студента
        GET /api/student-clubs/students/{id}/my_clubs/?lang=ru
        """
        student = self.get_object()
        serializer = self.get_serializer(student)
        return Response(serializer.data)


class ClubMembershipViewSet(BaseLanguageViewSet):
    """API для управления членством в клубах"""

    queryset = ClubMembership.objects.all()
    serializer_class = ClubMembershipSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["club", "student", "status"]

    def get_serializer_class(self):
        if self.action == "create":
            return ClubMembershipCreateSerializer
        return ClubMembershipSerializer

    def get_queryset(self):
        queryset = ClubMembership.objects.all().select_related("student", "club")

        # Фильтрация по статусу
        status = self.request.query_params.get("status")
        if status:
            statuses = status.split(",")
            queryset = queryset.filter(status__in=statuses)

        # Проверка на Swagger
        if getattr(self, "swagger_fake_view", False):
            return ClubMembership.objects.none()

        return queryset

    @action(detail=False, methods=["get"])
    def club_members(self, request):
        """
        Получить список членов клуба
        GET /api/student-clubs/memberships/club_members/?club=1&lang=ru&status=approved
        """
        club_id = request.query_params.get("club")
        if not club_id:
            return Response(
                {"error": "Параметр club обязателен"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Фильтруем по клубу
        try:
            club = Club.objects.get(pk=club_id)
        except Club.DoesNotExist:
            return Response(
                {"error": "Клуб не найден"}, status=status.HTTP_404_NOT_FOUND
            )

        # Применяем фильтрацию по статусу
        member_status = request.query_params.get("status", "approved")
        queryset = self.get_queryset().filter(club=club, status=member_status)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["post"])
    def join_club(self, request):
        """
        Присоединиться к клубу (создание запроса)
        POST /api/student-clubs/memberships/join_club/
        Body: {
          "student_id": 1,
          "club_id": 1,
          "motivation_text": "Хочу улучшить навыки программирования"
        }
        """
        serializer = ClubMembershipCreateSerializer(data=request.data)
        if serializer.is_valid():
            # Проверяем, существует ли уже членство
            student_id = serializer.validated_data.get("student").id
            club_id = serializer.validated_data.get("club").id

            # Если уже существует членство, возвращаем ошибку
            if ClubMembership.objects.filter(
                student_id=student_id, club_id=club_id
            ).exists():
                return Response(
                    {"error": "Вы уже отправили заявку на вступление в этот клуб"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Создаем новое членство со статусом pending
            membership = serializer.save(status="pending")

            # Обновляем счетчик участников клуба
            club = membership.club
            club.members_count = ClubMembership.objects.filter(
                club=club, status__in=["approved", "leader"]
            ).count()
            club.save()

            return Response(
                {
                    "success": True,
                    "message": "Заявка на вступление отправлена",
                    "membership_id": membership.id,
                    "status": membership.status,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"])
    def update_status(self, request, pk=None):
        """
        Обновить статус членства (для администраторов и лидеров клубов)
        POST /api/student-clubs/memberships/{id}/update_status/
        Body: {"status": "approved"}
        """
        membership = self.get_object()
        new_status = request.data.get("status")

        if not new_status or new_status not in [
            s[0] for s in ClubMembership.STATUS_CHOICES
        ]:
            return Response(
                {"error": "Некорректный статус"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Обновляем статус
        membership.status = new_status
        membership.save()

        # Обновляем счетчик участников клуба
        club = membership.club
        club.members_count = ClubMembership.objects.filter(
            club=club, status__in=["approved", "leader"]
        ).count()
        club.save()

        return Response(
            {
                "success": True,
                "message": f"Статус обновлен на {membership.get_status_display()}",
                "status": membership.status,
            }
        )
