from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MasterProgramsSerializer, FacultySerializer

from .models import MasterPrograms, Faculty

# Create your views here.
class MasterProgramsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MasterPrograms.objects.all()
    serializer_class = MasterProgramsSerializer

    def get_serializer_context(self):
            context = super().get_serializer_context()
            context['language'] = self.request.query_params.get('lang', 'ru')
            return context
    
class FacultyViewSet(viewsets.ReadOnlyModelViewSet):
      queryset = Faculty.objects.all()
      serializer_class = FacultySerializer

      def get_serializer_context(self):
            context = super().get_serializer_context()
            context['language'] = self.request.query_params.get('lang', 'ru')
            return context