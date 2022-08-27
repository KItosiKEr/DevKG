from dataclasses import field, fields
from rest_framework.serializers import ModelSerializer
from .models import Vacancies, Events, Video, Organization


class VacanciesSerializers(ModelSerializer):
    class Meta:
        model = Vacancies
        fields = ['id','company','job_title',
        'salary','type_of',
        'description','email','organization2']
        

class EventsSerializers(ModelSerializer):
    class Meta:
        model = Events
        fields = ['id','title','when','organizer',
                  'location','description','organization']

   
class VideoSerializers(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
   
    
class OrganizationSerializers(ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'image','name','description','web_site',
            'vacancies_p', 'videos_p', 'events_p',
        ]


class OrganizationDetailSerializers(ModelSerializer):
    vacancies = VacanciesSerializers(read_only=True, many=True)
    videos = VideoSerializers(read_only=True, many=True)
    events = EventsSerializers(read_only=True, many=True)

    class Meta:
        model = Organization
        fields = [
            'id',
            'image','name','description','web_site',
            'vacancies', 'videos', 'events',
        ]




# class CompanySerializers(ModelSerializer):
#     class Meta:
#         model = Company
#         fields = ['events1']