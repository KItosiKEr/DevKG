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
from django.http import HttpResponse  
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import filters
       
def my_mail(request):  
        subject = "Greetings from Programink"  
        msg     = "Learn Django at Programink.com"  
        to      = "hello@programink.com"  
        res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
        if(res == 1):  
            msg = "Mail Sent Successfully."  
        else:  
            msg = "Mail Sending Failed."  
        return HttpResponse(msg)  


class VacanciesView(ModelViewSet):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['company', 'email']


    

class EventsView(ModelViewSet):
    queryset = Events.objects.order_by('when').all()
    serializer_class = EventsSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class VideoView(ModelViewSet):
    queryset = Video.objects.order_by('created_date').all()
    serializer_class = VideoSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, ]
   

class OrganizationView(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, ]
#функция для просмотра делатьной информации 
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrganizationDetailSerializers
        return super().get_serializer_class()


# class CompanyView(ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializers


# Create your views here.
