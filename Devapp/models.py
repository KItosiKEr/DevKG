from ast import Or
from random import choices
import re
from tabnanny import verbose
from django.db import models
from transliterate import translit
from django.utils import timezone
from .conf import *


class Organization(models.Model):
    image = models.ImageField(upload_to='YouTube.IM/%Y/%m',)
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
    title = models.TextField(verbose_name='название')
    when = models.DateTimeField(blank=True, null=True, verbose_name='когда')
    organizer = models.CharField(max_length=20, verbose_name='организатор')
    location = models.TextField(verbose_name='локация')
    description = models.TextField(blank=True, verbose_name='описание')
    

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


def upload_location(instance,filename):
  return "%s/%s" %('video',translit('video','ru',reversed=True))



class Video(models.Model):
    organization1 = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='videos')
    title = models.TextField(verbose_name='название')
    organization = models.CharField(max_length=50, verbose_name='организация')
    video = models.FileField(upload_to='upload_location', blank=True, null=True, verbose_name='видео')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='дата публикации')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Vacancies(models.Model):
    organization2 = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='vacancies')
    company = models.CharField(max_length=50, verbose_name='компания')
    job_title = models.CharField(max_length=50,verbose_name='тип')
    salary = models.TextField(verbose_name='должность')
    type_of = models.CharField(max_length=50, verbose_name='валюта', choices=CURRENCY)
    type_of_2 = models.CharField(max_length=50, verbose_name='оклад')
    description = models.TextField(verbose_name='описание')
    email = models.EmailField(max_length=50,blank=True, verbose_name='E-mail')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
    # organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='vacancies')


# Create your models here.
