from ast import Or
import re
from tabnanny import verbose
from django.db import models
from transliterate import translit
from django.utils import timezone


class Organization(models.Model):
    image = models.ImageField(upload_to='YouTube.IM/%Y/%m')
    name = models.CharField(max_length=100)
    description = models.TextField()
    web_site = models.CharField(max_length=100)

    @property
    def events_p(self):
        return self.events.count()

    @property
    def vacancies_p(self):
        return self.vacancies.count()

    @property
    def videos_p(self):
        return self.videos.count()



class Events(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='events')
    title = models.TextField()
    when = models.TextField()
    organizer = models.CharField(max_length=20)
    location = models.TextField()
    description = models.TextField(blank=True)
    

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


def upload_location(instance,filename):
  return "%s/%s" %('video',translit('video','ru',reversed=True))



class Video(models.Model):
    organization1 = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='videos')
    title = models.TextField()
    organization = models.CharField(max_length=50)
    video = models.FileField(upload_to='upload_location', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
            self.published_date = timezone.now()
            self.save()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


# class Organization(models.Model):
#     image = models.ImageField(upload_to='YouTube.IM/%Y/%m')
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     web_site = models.CharField(max_length=100)

    
    # vacancies = models.ForeignKey(Vacancies, on_delete=models.CASCADE, related_name='organization')

    # @property
    # def organozation(self):
    #      print(self.organozation.all().count())

    # @property
    # def organization(self):
    #     return self.organization.all().count()

class Vacancies(models.Model):
    organization2 = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='vacancies')
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    salary = models.TextField()
    type_of = models.CharField(max_length=50)
    description = models.TextField()
    email = models.EmailField(max_length=50,blank=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
    # organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='vacancies')


# Create your models here.
