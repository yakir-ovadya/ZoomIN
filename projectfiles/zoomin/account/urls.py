# accounts/urls.py
from django.urls import path

from .views import schedule, register, grades, bulletin_board, bulletin_Schedule, presence, schedule, Username_Recovery, \
    bulletin_board_class, addBoardSchool, editBoardSchool, deleteBoardSchool,addBoardClass,editBoardClass,deleteBoardClass,\
    addSchedule, editSchedule, deleteSchedule, addTest, deleteTest, editTest, SearchResultsView, editSearch, deleteSearch,\
    addpresence, editpresence, showthis, editpre, show_grades, gradesedit
urlpatterns = [
    path('signup', register, name='signup'),

    path('bulletinboard', bulletin_board, name='bulletin_board'),
    path('bulletin_Schedule', bulletin_Schedule, name='bulletin_Schedule'),

    path('presence/', showthis.as_view(), name='presence'),
    path('presence/editpre/<int:id>', editpre, name='editpre'),
    path('presence/addpresence', addpresence, name='addpresence'),

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

    path('bulletin_Schedule/addbulletintest', addTest, name='addTest'),
    path('bulletin_Schedule/editTest/<int:id>', editTest, name='editTest'),
    path('bulletin_Schedule/deleteTest/<int:id>', deleteTest, name='deleteTest'),

    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search/editSearch/<int:id>', editSearch, name='editSearch'),
    path('search/deleteSearch/<int:id>', deleteSearch, name='deleteSearch'),

    path('grades', show_grades.as_view(), name='grades'),
    path('grades/gradesedit/<int:id>', gradesedit , name='gradesedit'),




]



