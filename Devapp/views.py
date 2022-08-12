from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import VacanciesSerializers, EventsSerializers, VideoSerializers, OrganizationSerializers
from rest_framework import permissions
from .models import Vacancies, Events, Video, Organization

class VacanciesView(ModelViewSet):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializers
    permission_classes = [permissions.IsAuthenticated]

class EventsView(ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializers
    permission_classes = [permissions.IsAuthenticated]

class VideoView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
    permission_classes = [permissions.IsAuthenticated]


class OrganizationView(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializers
    permission_classes = [permissions.IsAuthenticated]
# Create your views here.
