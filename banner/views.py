from rest_framework import generics
from rest_framework.response import Response
from .models import BannerSlide
from .serializers import BannerSlideSerializer

class BannerSlideListAPIView(generics.ListAPIView):
    serializer_class = BannerSlideSerializer
    
    def get_queryset(self):
        return BannerSlide.objects.filter(is_active=True).order_by('order')
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'slides': serializer.data
        })