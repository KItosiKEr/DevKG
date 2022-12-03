from rest_framework.serializers import ModelSerializer
from .models import Vacancies, Events, Video, Organization, SendMail


class VacanciesSerializers(ModelSerializer):
    class Meta:
        model = Vacancies
        fields = ['id','company','job_title',
        'salary','type_of','type_of_2',
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
# поля для детального просмотра
    class Meta:
        model = Organization
        fields = [
            'id',
            'image','name','description','web_site',
            'vacancies', 'videos', 'events',
        ]

class SendMailSerializer(ModelSerializer):
    class Meta:
        model = SendMail
        fields = ('full_name', 'email', 'message', 'phone_number', 'date')
        read_only_fields = ('date',)
        
    def create(self, validated_data):
        send_mail_to_email.delay(
            validated_data['full_name'],
            validated_data['email'],
            validated_data['message'],
            validated_data['phone_number'])
        return super().create(validated_data)


# class CompanySerializers(ModelSerializer):
#     class Meta:
#         model = Company
#         fields = ['events1']
