# schedule/urls.py
from django.urls import path

from .views import ScheduleView, HomeAfterLogin


urlpatterns = [
    path('/schedule', ScheduleView.as_view(), name='schedule'),
    path('', HomeAfterLogin.as_view(), name='schedule'),
]