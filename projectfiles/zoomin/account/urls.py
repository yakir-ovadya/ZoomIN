# accounts/urls.py
from django.urls import path

from .views import SignUpView, grades, bulletin_board, calendar, presence, schedule, Username_Recovery, \
    bulletin_board_class, addBoardSchool, editBoardSchool, deleteBoardSchool

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('grades/', grades, name='grades'),
    path('bulletinboard/', bulletin_board, name='bulletin_board'),
    path('calendar/', calendar, name='calendar'),
    path('presence/', presence, name='presence'),
    path('schedule/', schedule, name='schedule'),
    path('UsernameRecovery/', Username_Recovery, name='UsernameRecovery'),
    path('bulletinboardclass/', bulletin_board_class, name='bulletin_board_class'),
    path('bulletinboard/addbulletinboardSchool', addBoardSchool, name='addBoardSchool'),
    path('bulletinboard/editBoardSchool/<int:id>', editBoardSchool, name='editBoardSchool'),
    path('bulletinboard/deleteBoardSchool/<int:id>', deleteBoardSchool, name='deleteBoardSchool'),

]