from dataclasses import fields
from rest_framework.serializers import ModelSerializer

from .models import Vacancies, Events, Video, Organization

class VacanciesSerializers(ModelSerializer):
    class Meta:
        model = Vacancies
        fields = '__all__'

class EventsSerializers(ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

class VideoSerializers(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
    
class OrganizationSerializers(ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'