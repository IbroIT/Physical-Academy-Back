from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .models import Event
from .serializers import EventSerializer, EventListSerializer

class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.filter(is_active=True).order_by('order', '-created_at')
    serializer_class = EventListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'department', 'is_featured']

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Фильтрация по будущим/прошедшим мероприятиям
        timeframe = self.request.query_params.get('timeframe', None)
        if timeframe == 'upcoming':
            queryset = queryset.filter(date__gte=timezone.now().date())
        elif timeframe == 'past':
            queryset = queryset.filter(date__lt=timezone.now().date())
            
        return queryset

class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class FeaturedEventListAPIView(generics.ListAPIView):
    serializer_class = EventListSerializer
    
    def get_queryset(self):
        return Event.objects.filter(is_active=True, is_featured=True).order_by('order', '-created_at')

class EventCategoryListAPIView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        categories = []
        for choice in Event.CATEGORY_CHOICES:
            # Создаем переводы для каждого языка
            category_name = str(choice[1])
            categories.append({
                'id': choice[0],
                'name': {
                    'ru': category_name,
                    'en': self._translate_category(choice[0], 'en'),
                    'kg': self._translate_category(choice[0], 'kg')
                }
            })
        return Response(categories)
    
    def _translate_category(self, category_id, lang):
        """Перевод категорий на разные языки"""
        translations = {
            'conference': {
                'en': 'Conference',
                'kg': 'Конференция'
            },
            'seminar': {
                'en': 'Seminar', 
                'kg': 'Семинар'
            },
            'workshop': {
                'en': 'Workshop',
                'kg': 'Воркшоп'
            },
            'lecture': {
                'en': 'Lecture',
                'kg': 'Лекция'
            },
            'exhibition': {
                'en': 'Exhibition',
                'kg': 'Выставка'
            },
            'competition': {
                'en': 'Competition',
                'kg': 'Соревнование'
            },
            'festival': {
                'en': 'Festival',
                'kg': 'Фестиваль'
            },
            'sports': {
                'en': 'Sports',
                'kg': 'Спорт'
            },
            'cultural': {
                'en': 'Cultural Event',
                'kg': 'Маданий иш-чара'
            },
            'other': {
                'en': 'Other',
                'kg': 'Башка'
            }
        }
        return translations.get(category_id, {}).get(lang, category_id)

class EventDepartmentListAPIView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        departments = []
        for choice in Event.DEPARTMENT_CHOICES:
            department_name = str(choice[1])
            departments.append({
                'id': choice[0],
                'name': {
                    'ru': department_name,
                    'en': self._translate_department(choice[0], 'en'),
                    'kg': self._translate_department(choice[0], 'kg')
                }
            })
        return Response(departments)
    
    def _translate_department(self, department_id, lang):
        """Перевод отделов на разные языки"""
        translations = {
            'computer_science': {
                'en': 'Faculty of Computer Science',
                'kg': 'Компьютердик илимдер факультети'
            },
            'engineering': {
                'en': 'Engineering Faculty',
                'kg': 'Инженердик факультет'
            },
            'business': {
                'en': 'Business Faculty', 
                'kg': 'Бизнес факультети'
            },
            'medicine': {
                'en': 'Medical Faculty',
                'kg': 'Медицина факультети'
            },
            'arts': {
                'en': 'Faculty of Arts',
                'kg': 'Искусство факультети'
            },
            'science': {
                'en': 'Science Faculty',
                'kg': 'Илим факультети'
            },
            'law': {
                'en': 'Law Faculty',
                'kg': 'Укук факультети'
            },
            'international': {
                'en': 'International Department',
                'kg': 'Эл аралык бөлүм'
            },
            'student_union': {
                'en': 'Student Union',
                'kg': 'Студенттик союз'
            }
        }
        return translations.get(department_id, {}).get(lang, department_id)