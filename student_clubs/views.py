from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Club, ClubCategory, ClubLeader, ClubStats
from .serializers import (
    ClubListSerializer, ClubDetailSerializer, 
    ClubCategorySerializer, ClubLeaderSerializer,
    ClubStatsSerializer, ClubPageSerializer
)


class BaseLanguageViewSet(viewsets.ModelViewSet):
    """Базовый ViewSet с поддержкой языка"""
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        # Получаем язык из query параметров или заголовков
        language = self.request.query_params.get('lang', 
                   self.request.headers.get('Accept-Language', 'ru'))
        
        # Поддерживаем только ru, en, kg
        if language not in ['ru', 'en', 'kg']:
            language = 'ru'
        
        context['language'] = language
        return context


class ClubCategoryViewSet(BaseLanguageViewSet):
    """API для категорий клубов"""
    queryset = ClubCategory.objects.all()
    serializer_class = ClubCategorySerializer
    lookup_field = 'slug'
    
    def get_queryset(self):
        return ClubCategory.objects.all().order_by('order', 'name_ru')


class ClubViewSet(BaseLanguageViewSet):
    """API для клубов с фильтрацией и поиском"""
    queryset = Club.objects.filter(is_active=True)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'status', 'category__slug']
    search_fields = ['name_ru', 'name_en', 'name_kg', 'description_ru', 'description_en', 'description_kg', 'tags']
    ordering_fields = ['members_count', 'created_at', 'order']
    ordering = ['order', '-members_count']
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClubDetailSerializer
        return ClubListSerializer
    
    def get_queryset(self):
        queryset = Club.objects.filter(is_active=True).select_related('category').prefetch_related('leaders')
        
        # Фильтрация по категории через slug
        category_slug = self.request.query_params.get('category')
        if category_slug and category_slug != 'all':
            queryset = queryset.filter(category__slug=category_slug)
        
        # Фильтрация по статусу
        club_status = self.request.query_params.get('status')
        if club_status:
            queryset = queryset.filter(status=club_status)
        
        # Поиск по названию и описанию на всех языках
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(name_ru__icontains=search) |
                Q(name_en__icontains=search) |
                Q(name_kg__icontains=search) |
                Q(description_ru__icontains=search) |
                Q(description_en__icontains=search) |
                Q(description_kg__icontains=search) |
                Q(tags__icontains=search)
            )
        
        return queryset
    
    @action(detail=False, methods=['get'])
    def page_data(self, request):
        """
        Возвращает все данные для страницы клубов: заголовки, статистику, категории и клубы
        GET /api/clubs/page_data/?lang=ru
        """
        language = self.get_serializer_context()['language']
        
        # Переводы заголовков
        titles = {
            'ru': {
                'title': 'Студенческие клубы и сообщества',
                'subtitle': 'Присоединяйтесь к клубам и развивайте свои навыки вместе с единомышленниками'
            },
            'en': {
                'title': 'Student Clubs and Communities',
                'subtitle': 'Join clubs and develop your skills with like-minded people'
            },
            'kg': {
                'title': 'Студенттик клубдар жана коомдор',
                'subtitle': 'Клубдарга кошулуңуз жана бир ой адамдар менен көндүмдөрүңүздү өнүктүрүңүз'
            }
        }
        
        # Получаем данные
        stats = ClubStats.objects.filter(is_active=True).order_by('order')
        categories = ClubCategory.objects.all().order_by('order')
        clubs = self.get_queryset()
        
        # Применяем фильтры из запроса
        category_filter = request.query_params.get('category')
        if category_filter and category_filter != 'all':
            clubs = clubs.filter(category__slug=category_filter)
        
        search_filter = request.query_params.get('search')
        if search_filter:
            clubs = clubs.filter(
                Q(name_ru__icontains=search_filter) |
                Q(name_en__icontains=search_filter) |
                Q(name_kg__icontains=search_filter) |
                Q(description_ru__icontains=search_filter) |
                Q(description_en__icontains=search_filter) |
                Q(description_kg__icontains=search_filter)
            )
        
        context = self.get_serializer_context()
        
        data = {
            'title': titles.get(language, titles['ru'])['title'],
            'subtitle': titles.get(language, titles['ru'])['subtitle'],
            'stats': ClubStatsSerializer(stats, many=True, context=context).data,
            'categories': ClubCategorySerializer(categories, many=True, context=context).data,
            'clubs': ClubListSerializer(clubs, many=True, context=context).data,
        }
        
        return Response(data)
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """
        Получить клубы по категории
        GET /api/clubs/by_category/?category=tech&lang=ru
        """
        category_slug = request.query_params.get('category')
        if not category_slug:
            return Response(
                {'error': 'Category parameter is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        queryset = self.get_queryset().filter(category__slug=category_slug)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        """
        Присоединиться к клубу (отправка данных)
        POST /api/clubs/{id}/join/
        Body: {"email": "user@example.com", "name": "John Doe"}
        """
        club = self.get_object()
        
        # Здесь можно добавить логику сохранения заявки
        # Например, отправка email, сохранение в БД и т.д.
        
        return Response({
            'success': True,
            'message': f'Заявка на вступление в клуб "{club.name_ru}" отправлена',
            'club_name': club.get_field('name', self.get_serializer_context()['language']),
            'join_link': club.join_link
        })


class ClubLeaderViewSet(BaseLanguageViewSet):
    """API для руководителей клубов"""
    queryset = ClubLeader.objects.all()
    serializer_class = ClubLeaderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['club']
    
    def get_queryset(self):
        return ClubLeader.objects.select_related('club').order_by('order', 'name_ru')


class ClubStatsViewSet(BaseLanguageViewSet):
    """API для статистики клубов"""
    queryset = ClubStats.objects.filter(is_active=True)
    serializer_class = ClubStatsSerializer
    http_method_names = ['get']  # Только чтение
    
    def get_queryset(self):
        return ClubStats.objects.filter(is_active=True).order_by('order')
