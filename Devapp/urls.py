from xml.etree.ElementInclude import include
from django.urls import path

from .views import EventsView, VacanciesView, VideoView, OrganizationView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/v1/vacancies', VacanciesView)
router.register('api/v1/events', EventsView)
router.register('apu.v1/video', VideoView)
router.register('api/v1/organization', OrganizationView)
urlpatterns = router.urls