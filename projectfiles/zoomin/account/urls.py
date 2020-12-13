# accounts/urls.py
from django.urls import path

from .views import SignUpView
from .views import Username_Recovery

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('UsernameRecovery/', SignUpView.as_view(), name='UsernameRecovery'),
]