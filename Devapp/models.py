from dataclasses import field
from tabnanny import verbose
from django.db import models

class Vacancies(models.Model):
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    salary = models.TextField()
    type_of = models.CharField(max_length=50)
    description = models.TextField()
    email = models.EmailField(max_length=50)

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


# Create your models here.
