from rest_framework import generics
from rest_framework.response import Response
from .models import Quote
from .serializers import QuoteSerializer

class QuoteListAPIView(generics.ListAPIView):
    serializer_class = QuoteSerializer
    
    def get_queryset(self):
        return Quote.objects.filter(is_active=True).order_by('order', 'created_at')
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response({
            'success': True,
            'quotes': serializer.data
        })