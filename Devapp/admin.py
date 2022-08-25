from django.contrib import admin
from .models import Vacancies, Events, Video, Organization


admin.site.register(Vacancies)
admin.site.register(Events)
admin.site.register(Video)
admin.site.register(Organization)


# Register your models here.
