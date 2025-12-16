from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import (
    MasterProgramsSerializer,
    CollegeProgramsSerializer,
    PhdProgramsSerializer,
)
from .models import MasterPrograms, CollegePrograms, PhdPrograms


class MasterProgramsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MasterPrograms.objects.all()
    serializer_class = MasterProgramsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class PhdProgramsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PhdPrograms.objects.all()
    serializer_class = MasterProgramsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class CollegeProgramsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CollegePrograms.objects.all()
    serializer_class = MasterProgramsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context



