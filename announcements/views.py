from rest_framework import generics
from rest_framework.response import Response
from .models import Announcement
from .serializers import AnnouncementSerializer

class AnnouncementListAPIView(generics.ListAPIView):
    serializer_class = AnnouncementSerializer
    
    def get_queryset(self):
        return Announcement.objects.filter(is_active=True).order_by('order', '-created_at')
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response({
            'success': True,
            'announcements': serializer.data
        })

class AnnouncementDetailAPIView(generics.RetrieveAPIView):
    queryset = Announcement.objects.filter(is_active=True)
    serializer_class = AnnouncementSerializer
    lookup_field = 'id'
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request': request})
        return Response({
            'success': True,
            'announcement': serializer.data
        })