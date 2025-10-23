from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
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
            categories.append({
                'id': choice[0],
                'name_ru': str(choice[1]),
                'name_en': choice[1],
                'name_ky': choice[1],
            })
        return Response(categories)

class EventDepartmentListAPIView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        departments = []
        for choice in Event.DEPARTMENT_CHOICES:
            departments.append({
                'id': choice[0],
                'name_ru': str(choice[1]),
                'name_en': choice[1],
                'name_ky': choice[1],
            })
        return Response(departments)