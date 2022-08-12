from dataclasses import field
from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from transliterate import translit

class Vacancies(models.Model):
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    salary = models.TextField()
    type_of = models.CharField(max_length=50)
    description = models.TextField()
    email = models.EmailField(max_length=50,blank=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

class Events(models.Model):
    title = models.TextField()
    when = models.TextField()
    organizer = models.CharField(max_length=20)
    location = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


def upload_location(instance,filename):
  return "%s/%s" %('video',translit(filename,'ru',reversed=True))


class Video(models.Model):
    title = models.TextField()
    date = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    video = models.FileField(upload_to=upload_location, blank=True, null=True)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Organization(models.Model):
    company = models.ForeignKey(Events, on_delete=models.CASCADE)




# Create your models here.
