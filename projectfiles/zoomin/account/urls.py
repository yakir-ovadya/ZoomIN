# accounts/urls.py
from django.urls import path

from .views import schedule, register, grades, bulletin_board, calendar, presence, schedule, Username_Recovery, \
    bulletin_board_class, addBoardSchool, editBoardSchool, deleteBoardSchool,addBoardClass,editBoardClass,deleteBoardClass,\
    addSchedule, editSchedule, deleteSchedule
urlpatterns = [
    path('signup', register, name='signup'),
    path('grades', grades, name='grades'),
    path('bulletinboard', bulletin_board, name='bulletin_board'),
    path('calendar', calendar, name='calendar'),
    path('presence', presence, name='presence'),
    path('usernamerecovery/', Username_Recovery, name='usernamerecovery'),
    path('schedule', schedule, name='schedule'),
    path('schedule/addschedule', addSchedule, name='addSchedule'),
    path('schedule/editschedule/<int:id>', editSchedule, name='editSchedule'),
    path('schedule/deleteschedule/<int:id>', deleteSchedule, name='deleteSchedule'),
    path('bulletinboardclass/', bulletin_board_class, name='bulletin_board_class'),
    path('bulletinboard/addbulletinboardSchool', addBoardSchool, name='addBoardSchool'),
    path('bulletinboard/editBoardSchool/<int:id>', editBoardSchool, name='editBoardSchool'),
    path('bulletinboard/deleteBoardSchool/<int:id>', deleteBoardSchool, name='deleteBoardSchool'),
    path('bulletinboard/addbulletinboardClass', addBoardClass, name='addBoardClass'),
    path('bulletinboard/editBoardClass/<int:id>', editBoardClass, name='editBoardClass'),
    path('bulletinboard/deleteBoardClass/<int:id>', deleteBoardClass, name='deleteBoardClass'),
]



