from rest_framework import generics
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer

class NewsListAPIView(generics.ListAPIView):
    serializer_class = NewsSerializer
    
    def get_queryset(self):
        return News.objects.filter(is_active=True).order_by('order', '-created_at')
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response({
            'success': True,
            'news': serializer.data
        })

class NewsDetailAPIView(generics.RetrieveAPIView):
    queryset = News.objects.filter(is_active=True)
    serializer_class = NewsSerializer
    lookup_field = 'id'
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request': request})
        return Response({
            'success': True,
            'news': serializer.data
        })