from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    VacanciesSerializers, EventsSerializers, 
    VideoSerializers, OrganizationSerializers, 
    OrganizationDetailSerializers
)
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Vacancies, Events, Video, Organization
from rest_framework import generics


class VacanciesView(ModelViewSet):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, ]

class EventsView(ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, ]

class VideoView(ModelViewSet):
    queryset = Video.objects.order_by('published_date')
    serializer_class = VideoSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['date']



class OrganizationView(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrganizationDetailSerializers
        return super().get_serializer_class()


# class CompanyView(ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializers


# Create your views here.
