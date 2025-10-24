from rest_framework import generics
from rest_framework.response import Response
from .models import Fact
from .serializers import FactSerializer

class FactListAPIView(generics.ListAPIView):
    serializer_class = FactSerializer
    
    def get_queryset(self):
        return Fact.objects.filter(is_active=True).order_by('order', 'created_at')
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response({
            'success': True,
            'facts': serializer.data
        })