from .views import EventsView, VacanciesView, VideoView, OrganizationView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()

router.register('api/v1/vacancies', VacanciesView)
router.register('api/v1/events', EventsView)
router.register('apu/v1/video', VideoView)
router.register('api/v1/organization', OrganizationView)


urlpatterns = [
    # path('org-list', OrganizationView.as_view()),
    # path('even-list', EventsView.as_view())
]

urlpatterns = router.urls
